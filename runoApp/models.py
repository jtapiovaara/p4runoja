from django.db import models

# Create your models here.

class RunoDB(models.Model):
    picture = models.CharField(max_length=64, blank=True)
    name = models.CharField(max_length=64)
    caption = models.TextField(max_length=480, blank=True)
    author = models.CharField(max_length=32, blank=True)
    rate = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.name
