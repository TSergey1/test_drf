from django.contrib import admin
from event.models import Event, Organization
from users.models import User


class UserInline(admin.TabularInline):
    model = User.organizations.through
    extra = 2


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'postcode',
        'address'
    )
    inlines = (UserInline,)
    list_display = ('title', 'all_address')
    list_filter = ('title',)
    search_fields = ('title',)


class OrganizationInline(admin.TabularInline):
    model = Organization.events.through
    extra = 2


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    inlines = (OrganizationInline,)
    fields = (
        'title',
        'description',
        'admin_image',
        'date',
    )
    list_display = (
        'title',
        'description',
        'admin_image',
        'date',
    )
    readonly_fields = ('admin_image',)
    list_filter = ('title',)
    search_fields = ('title', 'date',)


admin.site.empty_value_display = 'Не задано'
