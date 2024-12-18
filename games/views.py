from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Gamer, BoardGame, Loan
from .forms import BoardGameForm


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
    gamer = Gamer.objects.get(owner=request.user)
    games = BoardGame.objects.exclude()
    context = {'games': games, 'gamer': gamer}
    return render(request, 'games/games.html', context)


# View for game details and loan
@login_required
def game_detail(request, game_id):
    gamer = Gamer.objects.get(owner=request.user)
    game = get_object_or_404(BoardGame, id=game_id)
    context = {'game': game, 'gamer': gamer}
    return render(request, 'games/game_detail.html', context)


# View to create a new loan record
@login_required
def create_loan(request, board_game_id):
    board_game = get_object_or_404(BoardGame, id=board_game_id)
    gamer, created = Gamer.objects.get_or_create(owner=request.user)

    if created:
        messages.info(
            request, "Your Gamer profile has been created automatically.")

    if not gamer.can_borrow():
        messages.error(
            request, "You have reached the maximum limit of 3 borrowed games. Please return a game before borrowing another.")
        return redirect('games:index')

    if request.method == 'POST':
        Loan.objects.create(board_game=board_game, gamer=gamer)
        board_game.is_available = False
        board_game.save()
        messages.success(request, "Loan created successfully.")
        return redirect('games:loan_success')
    return render(request, 'games/create_loan.html', {'board_game': board_game})


# Loan success page view
@login_required
def loan_success(request):
    return render(request, 'games/loan_success.html')


# View to display all loans for the logged-in user
@login_required
def loans(request):
    gamer = get_object_or_404(Gamer, owner=request.user)
    loans = gamer.loans.all()
    context = {'loans': loans}
    return render(request, 'games/loans.html', context)


# View for a profile
@login_required
def profile(request):
    user = request.user
    games = BoardGame.objects.filter(owner__owner=user)
    loans = Loan.objects.filter(gamer__owner=user)
    active_loans = loans.filter(returned=False)
    context = {'user': user, 'games': games,
               'loans': loans, 'active_loans': active_loans}
    return render(request, 'games/profile.html', context)


# View to add a new game
@login_required
def add_game(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.owner = Gamer.objects.get(owner=request.user)
            game.save()
            return redirect('games:profile')
    else:
        form = BoardGameForm()
    return render(request, 'games/add_game.html', {'form': form})


# View to edit a game
@login_required
def edit_game(request, game_id):
    game = get_object_or_404(BoardGame, id=game_id, owner__owner=request.user)
    if request.method == 'POST':
        form = BoardGameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('games:profile')
    else:
        form = BoardGameForm(instance=game)
    return render(request, 'games/edit_game.html', {'form': form})


# View to delete a game
@login_required
def delete_game(request, game_id):
    game = get_object_or_404(BoardGame, id=game_id, owner__owner=request.user)
    if request.method == 'POST':
        game.delete()
        return redirect('games:profile')
    return render(request, 'games/delete_game.html', {'game': game})


# View to return a borrowed game
@login_required
@login_required
def return_game(request, loan_id):
    loan = get_object_or_404(
        Loan, id=loan_id, gamer__owner=request.user, returned=False)
    board_game = loan.board_game

    loan.returned = True
    loan.returned_date = timezone.now()
    loan.save()

    board_game.is_available = True
    board_game.save()

    messages.success(request, f"The game {
                     board_game.name} has been successfully returned and is now available for others.")
    return redirect('games:return_success')


@login_required
def return_success(request):
    return render(request, 'games/return_success.html')
