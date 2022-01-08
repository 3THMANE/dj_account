from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Registerform, Profileform
from .models import Profile


from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request,'home.html')

def teacher(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles':profiles})
def teacher_d(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'profile_d.html', {'profile':profile})

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            # user = User.objects.get(username=username)
        # except:
            # messages.error(request,'user does not exist')
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('profile')
        except:
            messages.error(request, 'check your input data')
    return render(request,'login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    return render(request,'account.html',{'profile':profile})


@login_required(login_url='login')
def editaccount(request):
    profile = request.user.profile
    form = Profileform(instance=profile)
    if request.method == 'POST':
        form = Profileform(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('account')
    return render(request,'edit-account.html',{'form':form})


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = Registerform()
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'error accroding registeration')

    return render(request,'login_register.html', {'form':form})