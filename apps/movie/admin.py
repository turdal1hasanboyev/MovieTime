from django.contrib import admin

from .models import Movie, MovieImage, Review, MovieFile, AdditionalInfo, Liked

admin.site.register(MovieImage)
admin.site.register(Review)
admin.site.register(MovieFile)
admin.site.register(AdditionalInfo)
admin.site.register(Liked)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'created_at',
    )

    prepopulated_fields = {"slug": ["name"]}    
