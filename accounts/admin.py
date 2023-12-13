from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Teacher,Subject
from .forms import UserRegisterForm

# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    add_form = UserRegisterForm
    model = CustomUser

    list_display = ["email", "fullname", "is_staff"]
    list_filter = ["is_staff","is_active"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["fullname","phone_number","profile"]}),
        ("Permissions", {"fields": ["is_staff","rules","is_active","is_teacher"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)


