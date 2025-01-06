from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

        
class UserRegistrationForm(UserCreationForm):
    # Adding custom fields
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

def save(self, commit=True):
        user = super().save(commit=False)
        # Additional processing (e.g., save email or full name)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user