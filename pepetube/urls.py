from django.urls import path
from . import views

app_name = 'pepetube'

urlpatterns = [
    path('', views.lista_videos, name='lista_videos'),
    path('ver/<int:pk>/', views.detalle_video, name='detalle_video'),
    path('crear/', views.crear_video, name='crear_video'),
    path('buscar/',views.buscar_videos, name='buscar_videos'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]