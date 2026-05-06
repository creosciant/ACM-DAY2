from django.db import models

class Score(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    GENRE_CHOICES = [
        ('ph', 'Philippines'),
        ('academic', 'Academic'),
        ('ent', 'Entertainment'),
    ]
    
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-score', '-created_at']
        indexes = [
            models.Index(fields=['genre', '-score']),
        ]
    
    def __str__(self):
        return f"{self.player_name} - {self.score} ({self.genre}, {self.difficulty})"
