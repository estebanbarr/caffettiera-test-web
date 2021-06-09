from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store')
]
