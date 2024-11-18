from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Gamer, BoardGame, Loan
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Home page view
@login_required
def index(request):
    return render(request, 'games/index.html')

# View for listing all gamers
@login_required
def gamers(request):
    gamers = Gamer.objects.order_by('joined_date') 
    context = {'gamers': gamers}
    return render(request, 'games/gamers.html', context)

# View for a single gamer's details
@login_required
def gamer(request, gamer_id):
    gamer = get_object_or_404(Gamer, id=gamer_id)
    board_games = gamer.board_games.all()
    loans = gamer.loans.all()
    context = {'gamer': gamer, 'board_games': board_games, 'loans': loans}
    return render(request, 'games/gamer.html', context)


# View for available and loaned games 
@login_required
def games(request):
    available_games = BoardGame.objects.filter(loans__isnull=True)  
    loaned_games = BoardGame.objects.filter(loans__isnull=False).distinct()  

    context = {
        'available_games': available_games,
        'loaned_games': loaned_games
    }

    return render(request, 'games/games.html', context)

# View for game details and loan
@login_required
def game_detail(request, game_id):
    game = get_object_or_404(BoardGame, id=game_id)
    is_available = not game.loans.exists() or game.loans.last().return_by < timezone.now()  
    
    context = {'game': game, 'is_available': is_available}
    return render(request, 'games/game_detail.html', context)



# View to create a new loan record
@login_required
def create_loan(request, board_game_id):
    board_game = get_object_or_404(BoardGame, id=board_game_id)
    gamer, created = Gamer.objects.get_or_create(owner=request.user)  

    if created:
        messages.info(request, "Your Gamer profile has been created automatically.")

    if not gamer.can_borrow():
        messages.error(request, "You have reached the maximum limit of 3 borrowed games. Please return a game before borrowing another.")
        return redirect('games:index')

    if request.method == 'POST':
        return_by_date = request.POST.get('return_by')
        Loan.objects.create(board_game=board_game, gamer=gamer, return_by=return_by_date)
        messages.success(request, "Loan created successfully.")
        return redirect('games:loan_success')

    return render(request, 'games/create_loan.html', {'board_game': board_game})



# Loan success page view
@login_required
def loan_success(request):
    return render(request, 'games/loan_success.html')

# View to display all loans (optional)
@login_required
def loans(request):
    gamer = get_object_or_404(Gamer, id=request.user.id)
    loans = gamer.loans.all()
    context = {'loans': loans}
    return render(request, 'games/loans.html', context)
