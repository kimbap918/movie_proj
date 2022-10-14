from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


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
