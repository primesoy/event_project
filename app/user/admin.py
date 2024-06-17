from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Eigene Klasse in der Admin"""
    list_display = ["id", "user_name", "role", "email", "is_active", "is_staff", "email_confirmed"]
    ordering = ["email"]
    readonly_fields = ["email_confirmed", "email_token"]

    # Die Fieldsets sind die optische Darstellung in der 
    # Adminoberfläche. Sie müssen an das eigene User-Model angepasst werden
    fieldsets = (
        (None, {"fields": ("password", "user_name")}),
        ("Personal info", {"fields": ("email", "role", "email_confirmed", "email_token")}), 
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),  # , "date_joined"
        # ("Additional info", {"fields": ("address",)}),
    )

    add_fieldsets = (
        (None, {"fields": ("password1", "password2")}),
        ("Personal info", {"fields": ("email", "role", "email_confirmed")}),  # "first_name", "last_name",
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        # ("Important dates", {"fields": ("last_login",)}),  # , "date_joined"
        # ("Additional info", {"fields": ("address",)}),
    )