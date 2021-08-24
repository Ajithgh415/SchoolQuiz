from django.db import models
from tkinter import CASCADE

class Result(models.Model):
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    endtime = models.CharField(max_length=20)
    # Create your models here.
