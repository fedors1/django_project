from django.contrib import admin
from blog.views import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("header", "description", "is_active")
    list_filter = ("created_at", "views_counter")
    search_fields = ("header", "description")
