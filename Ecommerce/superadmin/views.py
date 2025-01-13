from django.shortcuts import render 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse



 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    if not request.user.is_staff:  # Ensure the user is an admin
        return JsonResponse({'detail': 'Unauthorized: Admin access only'}, status=403)

    # Example response for the admin dashboard
    data = {
        'message': 'Welcome to the admin dashboard!',
        'user': request.user.username,
    }
    return JsonResponse(data)

def dashboard_view(request):
    return render(request, 'dashboard.html')
 