from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PersonalNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ' | ' + self.content