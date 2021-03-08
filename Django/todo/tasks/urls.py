from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('new/', TaskCreate.as_view(), name='task_new'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
]
