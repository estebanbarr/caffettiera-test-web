from django.urls import path

from . import views

urlpatterns = [
    # urls del sitio
    path('blog/', views.blog, name='blog'),
    path('blog/category/<int:category_id>/', views.category, name='category')
]
