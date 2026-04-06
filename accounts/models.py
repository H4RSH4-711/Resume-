from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_recruiter = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
