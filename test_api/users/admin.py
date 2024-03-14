from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'email',
        'phone',
        'password',
        'is_staff',
        'is_superuser',
        'organizations'
    )
    list_display = ('email', 'phone', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser')

    class Meta:
        model = User
