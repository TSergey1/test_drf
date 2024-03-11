from django.contrib import admin

from .models import Events, Organization


@admin.register(Organization)
class OrganizationsAdmin(admin.ModelAdmin):
    # exclude = ['stores']
    # list_display = ('name', 'category',)
    # list_filter = ('category', )
    # search_fields = ('name', 'id')
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    # exclude = ['stores']
    # list_display = ('name', 'category',)
    # list_filter = ('category', )
    # search_fields = ('name', 'id')
    pass
