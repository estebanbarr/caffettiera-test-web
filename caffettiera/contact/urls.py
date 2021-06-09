from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('', views.contact, name='contact')
]
