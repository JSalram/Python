# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *


# Create your views here.
class TodoList(ListView):
    model = Task
    template_name = 'todo_list.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = '__all__'


class TaskDelete(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('todo_list')


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'task_edit.html'
    fields = '__all__'
