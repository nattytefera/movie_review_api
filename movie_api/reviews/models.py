from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.title}"
    
    def clean(self):
        if self.rating < 1 or self.rating > 5:
            return ValidationError("Rating must be between 1 and 5")
