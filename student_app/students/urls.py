

# students/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),          # URL for viewing/updating the profile
   # path('tasks/', views.task_list, name='task_list'),                # URL for listing tasks
    path('', views.task_create, name='task_create'),     # URL for creating a new task
    path('', views.task_update, name='task_update'),  # URL for updating a task
    path('', views.task_delete, name='task_delete'),  # URL for deleting a task
]
