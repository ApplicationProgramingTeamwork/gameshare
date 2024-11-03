from django.contrib import admin
from .models import Gamer,BoardGame,Loan

# Register your models here.
admin.site.register(Gamer)
admin.site.register(BoardGame)
admin.site.register(Loan)