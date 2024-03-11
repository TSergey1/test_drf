from django.contrib import admin

from .models import Event, Organization


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    exclude = ('description',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image',
        'date',
    )
    list_filter = ('title',)
    search_fields = ('title', 'date',)
