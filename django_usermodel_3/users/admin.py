from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUsuarioCreateForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("first_name", "last_name", "email", "phone", "is_staff")
    fieldsets = ( # yapf: disable
        (None, {'fields': ("email", "password")}),
        ("Informações Pessoais", {"fields": ("first_name", "last_name", "phone")}),
        ("Permissões", {"fields": ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Outros dados", {'fields': ('last_login', 'date_joined')})
    )