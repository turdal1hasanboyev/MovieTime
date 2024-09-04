from django.contrib import admin

from .models import MovieNews, Tag

admin.site.register(Tag)


@admin.register(MovieNews)
class MovieNewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'created_at',
    )

    prepopulated_fields = {"slug": ["name"]}
