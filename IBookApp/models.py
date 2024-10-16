from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return self.title
