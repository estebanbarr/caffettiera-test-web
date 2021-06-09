from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('services/', views.services, name='services')
]
