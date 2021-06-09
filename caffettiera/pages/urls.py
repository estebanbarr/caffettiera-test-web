from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('<int:page_id>/<slug:page_title>/', views.page, name='page')
]
