from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Handle the user registration process."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        # Process the filled-out form if the method is POST.
        form = UserCreationForm(data=request.POST)
        
        # Check if the form is valid.
        if form.is_valid():
            # Save the new user's data and create a new user instance.
            new_user = form.save()
            
            # Log in the new user immediately after registration.
            login(request, new_user)
            
            # Redirect to the homepage or another page after registration.
            return redirect('games:index')
    
    # Prepare the form to be rendered in the registration template.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
