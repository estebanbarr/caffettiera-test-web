from django.db import models

# Create your models here.
class Comment(models.Model):
    title      = models.CharField(max_length=128, verbose_name='Título')
    content    = models.TextField(verbose_name='Contenido')
    author     = models.CharField(max_length=128, verbose_name='Autor')
    created    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name        = 'comentario'
        verbose_name_plural = 'comentarios'
        ordering            = ["-created"]

    def __str__(self):
        return self.title + ' (by ' + self.author + ')'
