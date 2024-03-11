from django.contrib import admin

from .models import Event, Organization


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    exclude = ['description']
    list_filter = ('title', )
    search_fields = ('name', 'id')


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('category', )
    search_fields = ('name', 'id')
