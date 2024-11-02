from django.contrib import admin

# Register your models here.
from .models import Gamer,BoardGame,Loan
admin.site.register(Gamer)
admin.site.register(BoardGame)
admin.site.register(Loan)