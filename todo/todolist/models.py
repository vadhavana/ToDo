from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    task = models.CharField(max_length=50)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)


    def __str__(self):
        return self.task
    