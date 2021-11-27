from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password',
                  )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password',
                  )


class UpperField(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CustomUpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['password', 'email',]
                  
