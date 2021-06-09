from django.db import models

# Create your models here.
class Link(models.Model):
    key     = models.SlugField(verbose_name='Nombre Clave', max_length=128, unique=True) 
    name    = models.CharField(verbose_name='Red Social', max_length=128)
    url     = models.URLField(verbose_name='Enlace', max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name        = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering            = ["name"]

    def __str__(self):
        return self.name
