from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fechaCompletada = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Personalizar el panel de administrador
    def __str__(self):
        return self.titulo +' por '+ self.usuario.username