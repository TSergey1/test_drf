from django.contrib import admin

from .models import Event, Organization


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'postcode',
        'address'
    )
    list_display = ('title', 'all_address')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'admin_image',
        'date'
    )
    list_display = (
        'title',
        'description',
        'admin_image',
        'date'
    )
    readonly_fields = ('admin_image',)
    list_filter = ('title',)
    search_fields = ('title', 'date',)


admin.site.empty_value_display = 'Не задано'
