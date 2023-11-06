from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomAuthenticationForm

# Create your views here.
def signin(request):
    #if a user is already signed in, redirect away
    if request.user.is_authenticated:
        return redirect('/')
    
    #if method is post submit form data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = CustomAuthenticationForm(request.POST)
            return render(request, 'authentication/login.html', {'form': form})
    #else show the form to be filled in
    else:
        form = CustomAuthenticationForm()
        return render(request, 'authentication/login.html', {'form': form})


def signup(request):
    #if a user is already signed in, redirect away
    if request.user.is_authenticated:
        return redirect('/')
    
    #if method is post submit form data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'authentication/signup.html', {'form': form})
    #else show the form to be filled in
    else:
        form = UserCreationForm()
        return render(request, 'authentication/signup.html', {'form': form})
    
def logout(request):
    logout(request)
    return redirect('/')
