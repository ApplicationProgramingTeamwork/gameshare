from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Gamer model
class Gamer(models.Model):
    username = models.CharField(max_length=100, unique=True)  # Ensure unique usernames
    joined_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='gamers', on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def can_borrow(self):
        """Return True if the gamer can borrow a new game (maximum 3 games)."""
        return self.loans.count() < 3

# BoardGame model
class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('Gamer', related_name='board_games', on_delete=models.CASCADE)  # Use 'Gamer' as a string to avoid circular import
    genre = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='boardgame_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return self.name


# Loan model
class Loan(models.Model):
    board_game = models.ForeignKey('BoardGame', related_name='loans', on_delete=models.CASCADE)  # Use 'BoardGame' as a string to avoid circular import
    gamer = models.ForeignKey('Gamer', related_name='loans', on_delete=models.CASCADE)  # Use 'Gamer' as a string to avoid circular import
    loaned_at = models.DateTimeField(auto_now_add=True)
    return_by = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gamer.username} borrowed {self.board_game.name}"

    def is_overdue(self):
        """Return True if the loan is overdue."""
        return timezone.now() > self.return_by

    class Meta:
        ordering = ['-loaned_at']
        unique_together = ('board_game', 'gamer')  # Ensure each game is loaned to only one gamer at a time
