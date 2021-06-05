from django.urls import path

from . import views

urlpatterns = [
    path('', views.newsindex, name='newsindex'),
    path('category', views.category_index, name='category_index'),
    path('category/add', views.Create_Category, name='category_create'),
]
