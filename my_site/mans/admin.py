from django.contrib import admin

from .models import Man, Category

@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'time_create', 'time_update', 'is_published', 'category']
    list_filter = ['time_create', 'time_update', 'is_published', 'category']
    search_fields = ['title', 'content']
    #raw_id_fields = ['category']
    date_hierarchy = 'time_update'
    ordering = ['is_published', 'time_update']

admin.site.register(Category)