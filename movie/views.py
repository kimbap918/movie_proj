from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import ReviewForm
from .models import Review



# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'movie/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movie:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'movie/login.html', context)

def accounts(request):
    accounts = get_user_model().objects.order_by('-pk')
    context = {
        'accounts': accounts
    }
    return render(request, 'movie/accounts.html', context)


def detail(request, pk):
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
    }
  return render(request, 'movie/detail.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'movie/update.html', context)

def logout(request):
  auth_logout(request)
  return redirect('movie:index')

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie:community')
    else:        
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'movie/create.html', context=context)

def community(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'movie/community.html', context)
