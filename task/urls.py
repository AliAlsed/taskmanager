from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='task.index'),
    path('<int:id>', views.detail, name='task.detail'),
    path('news/', views.newshome, name='task.news'),
    path('tasks/', views.tasks, name='task.tasks'),
    path('news/<int:id>', views.newsdetail, name='task.news.detail')
]
