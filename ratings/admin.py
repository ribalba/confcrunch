from django.contrib import admin
from .models import Conference, Rating

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'unique_url')
    inlines = [RatingInline]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('conference', 'rating', 'email')
