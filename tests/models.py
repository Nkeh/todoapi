from django.db import models
from django.utils import timezone
import datetime


class ToDo(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    details = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
    