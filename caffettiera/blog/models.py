from django.db                  import models
from django.utils               import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name    = models.CharField(max_length=128, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name        = 'categoría'
        verbose_name_plural = 'categorías'
        ordering            = ["name"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title      = models.CharField(max_length=128, verbose_name='Título')
    content    = models.TextField(verbose_name='Contenido')
    published  = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now)
    image      = models.ImageField(verbose_name='Imagen', upload_to='blog', blank=True, null=True)
    author     = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created    = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated    = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name        = 'post'
        verbose_name_plural = 'posts'
        ordering            = ["-created"]

    def __str__(self):
        return self.title + ' (by ' + self.author.get_username() + ')'
