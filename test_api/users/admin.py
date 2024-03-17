from django.contrib import admin

from event.models import Organization
from users.models import User


class OrganizationInline(admin.TabularInline):
    model = Organization.users.through
    extra = 2


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
    inlines = (OrganizationInline,)
    list_display = ('email', 'phone', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser')

    class Meta:
        model = User
