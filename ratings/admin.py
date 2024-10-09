from django.contrib import admin
from .models import Conference, Rating

from import_export.admin import ImportExportModelAdmin
from import_export import resources

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0

class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'unique_url')
    inlines = [RatingInline]

@admin.register(Rating)
class RatingAdmin(ImportExportModelAdmin):
    list_display = ('conference', 'rating', 'email')
    resource_classes = [RatingResource]

