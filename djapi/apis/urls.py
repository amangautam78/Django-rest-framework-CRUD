from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview),
    path('task-list/', views.taskList),
    path('task-detail/<str:pk>/', views.taskDetail),
    path('task-create/', views.taskCreate),
    path('task-update/<str:pk>/', views.taskUpdate),
    path('task-delete/<str:pk>/', views.taskDelete),
]