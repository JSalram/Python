from django.db import models
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    body = models.CharField(
        verbose_name='cuerpo',
        max_length=255
    )

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('todo_list')
