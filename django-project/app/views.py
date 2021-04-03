from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import *
import requests
from .models import *
from .whatsapp import message

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else: 
                messages.info(request, "Username or password is incorrect")
        
        context = {}
        return render(request, 'login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user )
                return redirect("login")

        context = {'form': form}
        return render(request, 'signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    videos = DetectionVideo.objects.all()
    context = {"videos": videos}
    return render(request, 'dashboard.html', context)

def updateProfile(request):
    try: 
        profile = Profile.objects.get(user=request.user)
    
        print(request)
        form = ProfileForm(instance=Profile.objects.get(user=request.user))
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=request.user)
            print(request.user)
            print(form)
            if form.is_valid():
                profile = Profile.objects.get(user=request.user)
                profile.name = form.cleaned_data.get('name')
                profile.contact = form.cleaned_data.get('contact')
                profile.save()
                
                return redirect('profile')
    
        context = {'form': form, 'profile': profile}

        return render(request, 'updateprofile.html', context)
    except Profile.DoesNotExist:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'updateprofile.html')

def displayProfile(request):
    try: 
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    # print(p)
    context = {"profile": profile}

    return render(request, 'profile.html', context)

def get_location(request):
    if request.method == "POST":
        location = request.POST['location'].split(",")
        print(location)

        # Instance of Profile
        profile = Profile.objects.get(user=request.user)
        print(request.user)
        print(profile)
        response = requests.get(f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={location[1]}&longitude={location[0]}&localityLanguage=en")
        json_response = response.json()
        profile.lat = location[1]
        profile.long = location[0]
        for i in json_response:
            if i == 'continent':
                print(json_response[i])
            if i == 'countryName':
                print(json_response[i])
                profile.country = f'{json_response[i]}'
            if i == 'principalSubdivision':
                print(json_response[i])
                profile.state = f'{json_response[i]}'
            if i == 'city':
                print(json_response[i])
                profile.city = f'{json_response[i]}'
            if i == 'locality':
                print(json_response[i])
                profile.town = f'{json_response[i]}'
        print(profile)
        profile.save()
        return redirect("update_profile")
        # print(json_response)
        # print(User.objects.filter(user=request.username))
    context = {}

    return render(request, 'geomap.html', context)


def video_page(request): 
    if request.method == 'POST': 
        title = request.POST['title']
        video = request.POST['video']
        user = request.user
        content = DetectionVideo(title=title,video=video, user=user)
        content.save()
        return redirect('dashboard')

    return render(request, 'videoupload.html')


def video_detection(request, name):
    videos = DetectionVideo.objects.filter(title=name)
    context = {'videos': videos}
    return render(request, 'videodetect.html', context) 


def wapalert(request):
    if request.method == 'POST': 
        number = request.POST['number']
        content = request.POST['content']
        print(number, content)
        message(number, content)
    context = {}
    return render(request, 'sendmessage.html', context)