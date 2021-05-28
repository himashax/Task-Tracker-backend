from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.CharField(max_length = 10, primary_key = True, unique=True)
    task = models.CharField(max_length = 100)
    day = models.DateField(auto_now=False, auto_now_add=False)
    reminder = models.BooleanField(default=False)

    def __str__(self):
        return self.id