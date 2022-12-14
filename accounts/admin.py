from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group



class UserCustomAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'username', 'is_active', 'joined_date', 'last_login']
    list_filter = ['admin', 'superadmin']

    readonly_fields = ['joined_date', 'last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'username',)}),
        ('All Permissions', {'fields' : ('is_active', 'admin', 'superadmin')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserCustomAdmin)
admin.site.unregister(Group)

