from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
# from .models import User
from django.http import HttpResponse
# from .models import Pet
from django.http import Http404

def home(request):
    # pets = Pet.objects.all()
    # return HttpResponse('<p> success </p>')
    return render(request, 'homepage/homepage.html', )
#   will use render instead

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.level = form.cleaned_data.get('level')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'loginpage/signup.html', {'form': form})


# def login(request):
#         return render(request, 'loginpage/login.html', )



def profile(request):
    username1 = None
    if request.user.is_authenticated:
        username1 = request.user.username
        user = User.objects.get(username=username1)
    else:
        user = User.objects.get(username='Gyde_mert')
    return render(request, 'profilepage/user_profile.html', {'users': user})


def newsfeed(request):
        return render(request, 'newsfeedpage/feed.html', )