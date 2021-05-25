from django.db import models

# Create your models here.

class PassWord(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logged_user = models.CharField(max_length=60)