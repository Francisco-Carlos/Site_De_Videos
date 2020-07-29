from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Videos(models.Model):
    Titulo = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=100)
    Video = models.FileField(upload_to='videos')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo

class Perfil(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    NikeName = models.CharField(max_length=100)
    Historia = models.TextField(max_length=500,blank=True,null=True)
    Foto = models.ImageField(upload_to='videos')

    def __str__(self):
        return self.NikeName


class Coment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Videos,on_delete=models.CASCADE)
    Comentario = models.TextField()

    def __str__(self):
        return str(self.user)