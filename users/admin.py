from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *
from .forms import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']
    fieldsets = (
        (
            (('User'), {
                'fields': ('password', 'email')
            }),

            (('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }),
        ))
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
