from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'score', 'genre', 'difficulty', 'created_at')
    list_filter = ('genre', 'difficulty', 'created_at')
    search_fields = ('player_name',)
    ordering = ('-score', '-created_at')
