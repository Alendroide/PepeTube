from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    titulo = models.CharField(max_length=100)
    archivo_video = models.FileField(upload_to='videos/')
    archivo_imagen = models.ImageField(upload_to='imagenes/')
    fecha = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.titulo