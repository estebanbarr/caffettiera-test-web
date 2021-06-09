from django.db import models

# Create your models here.
class Service(models.Model):
    title     = models.CharField(max_length=128, verbose_name='Titulo')
    sub_title = models.CharField(max_length=128, verbose_name='Sub Titulo')
    content   = models.TextField(verbose_name='Contenido')
    image     = models.ImageField(verbose_name='Imagen', upload_to='services')
    order     = models.IntegerField(verbose_name='Orden')
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = 'servicio'
        verbose_name_plural = 'servicios'
        ordering            = ["order"]

    def __str__(self):
        return self.title + ' | ' + self.sub_title
