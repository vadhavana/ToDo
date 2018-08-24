from django.db import models

class post(models.Model):
    no = models.IntegerField(default=True)
    l = models.CharField(max_length=100)

    def __str__(self):
        return self.l
        