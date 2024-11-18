from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),  
    path('gamers/', views.gamers, name='gamers'), 
    path('gamers/<int:gamer_id>/', views.gamer, name='gamer'),  
    path('create_loan/<int:board_game_id>/', views.create_loan, name='create_loan'), 
    path('loan_success/', views.loan_success, name='loan_success'),  
    path('games/', views.games, name='games'),  
    path('games/<int:game_id>/', views.game_detail, name='game_detail'), 
    path('add_game/', views.add_game, name='add_game'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    path('game/<int:game_id>/delete/', views.delete_game, name='delete_game'),
    path('profile/', views.profile, name='profile'),  
]
