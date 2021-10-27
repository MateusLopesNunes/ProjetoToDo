from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('yourName/<str:name>', views.yourName, name='your-name'),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView),
    path('newTask/', views.newTask),
    path('edit/<int:id>', views.editTask),
    path('delete/<int:id>', views.deleteTask),
]
