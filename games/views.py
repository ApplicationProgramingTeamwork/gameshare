from django.shortcuts import render,redirect
from .models import Gamer,BoardGame,Loan
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request, 'games/index.html')

def gamers(request):
    gamers = Gamer.objects.order_by('joined_date')
    context = {'gamers': gamers}
    return render(request, 'games/gamers.html', context)

def gamer(request, gamer_id):
    gamer = Gamer.objects.get(id=gamer_id)
    board_games = gamer.board_games.all()
    loans = gamer.loans.all()
    context = {'gamer': gamer, 'board_games': board_games, 'loans': loans }
    return render(request, 'games/gamer.html', context)

def create_loan(request, board_game_id):
    board_game = BoardGame.objects.get(id=board_game_id)
    gamer = Gamer.objects.get(id=request.user.id)  

    if request.method == 'POST':
        return_by_date = request.POST['return_by']  
        loan = Loan.objects.create(board_game=board_game, gamer=gamer, return_by=return_by_date)
        return redirect('games:loan_success')  

    return render(request, 'create_loan.html', {'board_game': board_game})

def loan_success(request):
    return render(request, 'games/loan_success.html')