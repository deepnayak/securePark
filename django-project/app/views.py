import os
import sys
import inspect
import threading
from django.core import serializers
import csv, io
from time import sleep

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
pparentdir = os.path.dirname(parentdir)
ppparentdir = os.path.dirname(pparentdir)
sys.path.insert(0, pparentdir) 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http.response import StreamingHttpResponse
from .forms import *
import requests
from .models import *
from .whatsapp import message
from pathlib import Path
from detect import *
import asyncio
import difflib
from datetime import datetime
from django.conf import settings

MEDIA_DIR = settings.MEDIA_ROOT
# import detect as dt

frame = 0
frame1 = 0
t1 = 0
t2 = 0
license_plates = []
lplates = []
stop = False
stop1 = False

# def getWeek(request):
#     legal = DetectionResult.objects.filter(legal=False)
#     illegal = DetectionResult.objects.filter(legal=True)
#     legalCount = [0]*7
#     illegalCount = [0]*7
#     for x in legal:
#         legalCount[x.weekday()] += 1
#     for x in illegal:
#         illegalCount[x.weekday()] += 1
    

class Options:
    def __init__(self, weights=None, source=None, img_size=None, 
    conf_thres=None, iou_thres=None, device=None, view_img=None, save_txt=None, save_con=None, 
    nosave=None, classes=None, agnostic_nms=None, augment=None, update=None, project=None, name=None, 
    exist_ok=None) -> None:
        if weights is None:
            self.weights = 'yolov5s.pt'
        else:
            self.weights = weights
        if source is None:
            self.source = 'data/images'
        else:
            self.source = source
        if img_size is None:
            self.img_size = 640
        else:
            self.img_size = img_size
        if conf_thres is None:
            self.conf_thres = 0.25
        else:
            self.conf_thres = conf_thres
        if iou_thres is None:
            self.iou_thres = 0.45
        else:
            self.iou_thres = iou_thres
        if device is None:
            self.device = ''
        else:
            self.device = device
        if view_img is None:
            self.view_img = False
        else:
            self.view_img = view_img
        if save_txt is None:
            self.save_txt = False
        else:
            self.save_txt = save_txt
        if save_con is None:
            self.save_con = False
        else:
            self.save_con = save_con
        if nosave is None:
            self.nosave = False
        else:
            self.nosave = nosave
        if classes is None:
            self.classes = 0
        else:
            self.classes = classes
        if agnostic_nms is None:
            self.agnostic_nms = False
        else:
            self.agnostic_nms = agnostic_nms
        if augment is None:
            self.augment = False
        else:
            self.augment = augment
        if update is None:
            self.update = False
        else:
            self.update = update
        if project is None:
            os.path.abspath
            self.project = os.path.abspath(MEDIA_DIR+'detect')
        else:
            self.project = project
        if name is None:
            self.name = 'exp'
        else:
            self.name = name
        if exist_ok is None:
            self.exist_ok = False
        else:
            self.exist_ok = exist_ok
        
def frameGame(fr, curr):
    # print("Hereeeee")
    global frame
    global stop
    global lplates
    lplates = curr
    frame = fr
    return stop

def frameGame1(fr, curr):
    # print("Hereeeee")
    global frame1
    global stop1
    global lplates
    lplates = curr
    frame1 = fr
    return stop1

async def detectCurVid(name, request, video, title):
    # parser.add_argument('--weights', nargs='+', type=str, default='yolov5s.pt', help='model.pt path(s)')
    # parser.add_argument('--source', type=str, default='data/images', help='source')  # file/folder, 0 for webcam
    # parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    # parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    # parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    # parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    # parser.add_argument('--view-img', action='store_true', help='display results')
    # parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    # parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    # parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    # parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    # parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    # parser.add_argument('--augment', action='store_true', help='augmented inference')
    # parser.add_argument('--update', action='store_true', help='update all models')
    # parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    # parser.add_argument('--name', default='exp', help='save results to project/name')
    # parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')

    # if name == 0 or name.startswith('http:'):
    #     opt = Options(source=name, weights=os.path.abspath('../run/last.pt'))
    #     for i in detect(opt=opt):

    opt = Options(source='videos/'+name, weights=os.path.abspath('../run/last.pt'), name=title)
    global license_plates
    license_plates = detect(opt=opt)
    print(license_plates)

def live(request):
    timestamp = int(datetime.now().timestamp())
    context = {'timest': timestamp, 'ty': '0'}
    return render(request, 'live.html', context)

def remote(request):
    timestamp = int(datetime.now().timestamp())
    context = {'timest': timestamp, 'ty': 'video'}
    return render(request, 'remote.html', context)

def gen():
    while True:
    # for i in camera(opt=opt):
		# frame = camera.get_frame()
        # frame = detect(opt=opt)
        # sleep(0.5)
        # print("Here")
        global frame
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen1():
    while True:
    # for i in camera(opt=opt):
		# frame = camera.get_frame()
        # frame = detect(opt=opt)
        # sleep(0.5)
        # print("Here")
        global frame1
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')


def video_feed(request, timestamp):
    global stop
    stop = False
    opt = Options(source='0', weights=os.path.abspath('../run/last.pt'), name='webcam'+str(timestamp))
    t1 = threading.Thread(target=detect, name='t1', args=(False, opt, frameGame,))
    t1.start()
    sleep(10)
    # print("Hererere")
    return StreamingHttpResponse(gen(),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request, timestamp):
    global stop1
    stop1 = False
    opt = Options(source='http://192.168.43.1:8080/video', weights=os.path.abspath('../run/last.pt'))
    t2 = threading.Thread(target=detect, name='t2', args=(False, opt, frameGame1,))
    t2.start()
    sleep(10)
    return StreamingHttpResponse(gen1(),
					content_type='multipart/x-mixed-replace; boundary=frame')

def intermediate(request, timestamp, type):
    global stop
    global stop1
    stop = True
    stop1 = True
    user = request.user
    path = os.path.abspath(MEDIA_DIR+'detect/webcam'+str(timestamp)+'/' + str(type) + '.mp4')
    content = DetectionVideo(title="webcam"+str(timestamp), user=user, path=path)
    content.save()
    valid = [x.carno.replace(" ", "") for x in CarProfile.objects.filter(user=request.user)]
    for plate in lplates:
        if len(difflib.get_close_matches(plate, valid, cutoff=0.6)) > 0:
            DetectionResult.objects.create(carno=plate, user=request.user, video=content, legal=True, created=datetime.now())
        else:
            DetectionResult.objects.create(carno=plate, user=request.user, video=content, legal=False, created=datetime.now())
    illegal = DetectionResult.objects.filter(video=content)
    msg = "We found the following intruders in your society:\n"
    for x in illegal:
        msg += (x.carno + '\n')
    profile = Profile.objects.get(user=request.user)
    message(profile.contact, msg)
    return redirect('dashboard')
    
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
    logs = DetectionResult.objects.all()[::-1][:8]
    
    legal = DetectionResult.objects.filter(legal=True)
    illegal = DetectionResult.objects.filter(legal=False)
    legalCount = [0]*7
    illegalCount = [0]*7
    tlegal = len(legal)
    tillegal = len(illegal)
    t = tlegal + tillegal
    for x in legal:
        legalCount[x.created.weekday()] += 1
    for x in illegal:
        illegalCount[x.created.weekday()] += 1

    
    society = Profile.objects.get(user=request.user)
    context = {"logs": logs, "lcount": legalCount, "icount": illegalCount, "tlegal": tlegal, "tillegal": tillegal, "t": t, "sn": society}
    return render(request, 'dashboard.html', context)

def updateProfile(request):
    try: 
        profile = Profile.objects.get(user=request.user)
        users = CarProfile.objects.filter(user=request.user)
        print(users)
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
    
        context = {'form': form, 'profile': profile, 'users': users}

        return render(request, 'profile.html', context)
    except Profile.DoesNotExist:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile.html')

# def displayProfile(request):
#     try: 
#         profile = Profile.objects.get(user=request.user)
#     except Profile.DoesNotExist:
#         profile = None
#     # print(p)
#     context = {"profile": profile}

#     return render(request, 'profile.html', context)

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
        return redirect("profile")
        # print(json_response)
        # print(User.objects.filter(user=request.username))
    context = {}

    return render(request, 'geomap.html', context)


def uploadvideo(request): 
    if request.method == 'POST' and 'video' in request.FILES: 
        title = request.POST['title']
        video = request.FILES['video']
        user = request.user
        # print(os.path.abspath('./detect/'))
        path = os.path.abspath(MEDIA_DIR+'detect/'+title+'/' + request.FILES['video'].name)
        content = DetectionVideo(title=title, video=video, user=user, path=path)
        content.save()
        asyncio.run(detectCurVid(request.FILES['video'].name, request, content, title))
        valid = [x.carno.replace(" ", "") for x in CarProfile.objects.filter(user=request.user)]
        for plate in license_plates:
            if len(difflib.get_close_matches(plate, valid, cutoff=0.6)) > 0:
                DetectionResult.objects.create(carno=plate, user=request.user, video=content, legal=True, created=datetime.now())
            else:
                DetectionResult.objects.create(carno=plate, user=request.user, video=content, legal=False, created=datetime.now())
        illegal = DetectionResult.objects.filter(video=content)
        msg = "We found the following intruders in your society:\n"
        for x in illegal:
            msg += (x.carno + '\n')
        profile = Profile.objects.get(user=request.user)
        message(profile.contact, msg)
        return redirect('dashboard')

    return render(request, 'uploadvideo.html')


def video_detection(request, name):
    print(name)
    videos = DetectionVideo.objects.get(title=name)
    cars = DetectionResult.objects.filter(video=videos)
    # video_path = [os.path.join(os.getcwd(), "videos", x.path) for x in videos]
    print(videos.path)
    video_path = videos.path[videos.path.find(videos.title):len(videos.path)]
    # videos = os.path.join(os.getcwd(), videos.title)
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # print("hi from " + f"{BASE_DIR}")
    context = {'videos': video_path, 'cars': cars}
    print(videos)
    return render(request, 'videovideo.html', context) 
    

def wapalert(request):
    if request.method == 'POST': 
        number = request.POST['number']
        content = request.POST['content']
        videos = DetectionVideo.objects.get(title=name)
        cars = DetectionResult.objects.filter(video=videos)
        print(number, content)
        message(number, content)
    context = {}
    return render(request, 'sendmessage.html', context)


def logs(request):
    logs = DetectionResult.objects.filter(user=request.user)[::-1]
    vidName = [x.video.title for x in logs]
    logsJS = serializers.serialize("json", logs)
    context = {"logs": logs, "vidname": vidName, "logsJS": logsJS}
    return render(request, 'logs.html', context)

def stats(request):
    context = {}
    return render(request, 'stats.html', context)

# def addusers(request):
#     context = {}
#     return render(request, 'addusers.html', context)

def videolist(request):
    videos = DetectionVideo.objects.all()[::-1]
    context = {"videos": videos}
    return render(request, 'videolist.html', context)

    
def addusers(request):
    # declaring template

    template = "addcars.html"
    
    data = CarProfile.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, phone, carno, carmodel, carcolour',
        'profiles': data    
              }

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        users = CarProfile.objects.filter(user=request.user)
        context = {'users': users}
        print(users)
        return render(request, template, context)
    csv_file = request.FILES.get('file', False)
    # let's check if it is a csv file
    # if not csv_file.name.endswith('.csv'):
    #     messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    print(io_string)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = CarProfile.objects.update_or_create(
            user=request.user,
            name=column[0],
            phone=column[1],    
            carno=column[2],
            carmodel=column[3],
            carcolour=column[4],

        )
    users = CarProfile.objects.filter(user=request.user)
    # Get all users
    context = {'users': users}
    return render(request, template, context)
