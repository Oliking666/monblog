from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'thumbnail')
    readonly_fields = ('thumbnail',)  # Affiche la miniature en lecture seule
