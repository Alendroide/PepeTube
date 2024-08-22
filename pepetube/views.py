from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='pepetube:login')
def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pepetube:lista_videos')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pepetube:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='pepetube:login')
def logout_view(request):
    logout(request)
    return redirect('pepetube:login')

def lista_videos(request):
    videos = Video.objects.all()
    return render(request, 'lista_videos.html', {'videos': videos})

def buscar_videos(request):
    query = request.GET.get('query')
    if query:
        videos = Video.objects.filter(titulo__icontains=query)
    else:
        videos = Video.objects.all()
    return render(request, 'buscar_videos.html', {'videos': videos, 'query': query})

def detalle_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'detalle_video.html', {'video': video})

@login_required(login_url='pepetube:login')
def crear_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.usuario = request.user
            video = form.save()
            return redirect('pepetube:detalle_video', pk=video.pk)
    else:
        form = VideoForm(initial={'usuario': request.user})
    return render(request, 'crear_video.html', {'form': form})