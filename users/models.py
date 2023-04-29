from django.db import models
from django.contrib.auth.models import User
from dataset.models import DataSet
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='media/profile-img',blank=True,null=True)
    loacation = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username