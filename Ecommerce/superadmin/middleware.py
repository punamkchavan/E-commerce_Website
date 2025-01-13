from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
         
        if request.path.startswith('/admin_login/'):
            try:
                
                jwt_auth = JWTAuthentication()
                auth_result = jwt_auth.authenticate(request)

                if auth_result is None:
 
                    raise AuthenticationFailed('Invalid or missing token')

                user, token = auth_result

                
                if not user.is_staff:
                    return JsonResponse({'detail': 'Unauthorized: Admin access only'}, status=403)

                 
                request.user = user

            except AuthenticationFailed as e:
                return JsonResponse({'detail': str(e)}, status=401)

        
        response = self.get_response(request)
        return response
