from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('', views.comments, name='comments')
]
