from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm,UserAdminChangeForm
from .models import User

User = get_user_model()

class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('fin', 'active', 'staff', 'company_user', 'customer_user', 'admin')
    list_filter = ('active', 'staff', 'company_user', 'customer_user', 'icra_company', 'e_mahkama', 'admin',)
    fieldsets = (
        (None, {'fields': ('fin', 'password')}),
        ('Personal info', {'fields': ('username', 'sirname', 'email')}),
        ('Permissions', {'fields': ('active', 'staff', 'company_user', 'customer_user', 'icra_company', 'e_mahkama', 'admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'confirm')}
        ),
    )
    search_fields = ('fin', 'username', 'sirname', 'email')
    ordering = ('username', 'sirname')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)