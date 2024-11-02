from django.db import models
from django.utils import timezone

# Create your models here.
class Gamer(models.Model):
    usersname = models.CharField(max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usersname
    

    def can_borrow(self):
        """Check if the gamer can borrow a new game (maximum 3 games)."""
        return self.loans.count() < 3
    
    
class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Gamer, related_name='board_games', on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'boardgames'

    def __str__(self):
        return self.name
    
class Loan(models.Model):
    board_game = models.ForeignKey(BoardGame, related_name='loans', on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, related_name='loans', on_delete=models.CASCADE)
    loaned_at = models.DateTimeField(auto_now_add=True)
    return_by = models.DateTimeField()

    def __str__(self):
        return f"{self.gamer.usersname} borrowed {self.board_game.name}"

    def is_overdue(self):
        """Check if the loan is overdue."""
        return timezone.now() > self.return_by

