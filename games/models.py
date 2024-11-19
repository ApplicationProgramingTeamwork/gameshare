from django.db import models
from django.utils import timezone
from django.conf import settings

# Gamer model


class Gamer(models.Model):
    # Ensure unique usernames
    username = models.CharField(max_length=100, unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='gamers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username}'

    def can_borrow(self):
        """Return True if the gamer can borrow a new game (maximum 3 games)."""
        return self.loans.count() < 3

# BoardGame model


class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    # Use 'Gamer' as a string to avoid circular import
    owner = models.ForeignKey(
        'Gamer', related_name='board_games', on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='boardgame_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return f'{self.name}'


# Loan model
class Loan(models.Model):
    # Use 'BoardGame' as a string to avoid circular import
    board_game = models.ForeignKey(
        'BoardGame', related_name='loans', on_delete=models.CASCADE)
    # Use 'Gamer' as a string to avoid circular import
    gamer = models.ForeignKey(
        'Gamer', related_name='loans', on_delete=models.CASCADE)
    loaned_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gamer.username} borrowed {self.board_game.name}"

    class Meta:
        ordering = ['-loaned_at']
        
