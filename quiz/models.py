from django.db import models
from tkinter import CASCADE

# Create your models here.

class SignUp(models.Model):
    institutionname = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    principalname = models.CharField(max_length=100)
    principalno = models.CharField(max_length=20)
    los = models.CharField(max_length=100)



class CreateQuiz(models.Model):
    studentname = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    std = models.CharField(max_length=20)
    gender = models.CharField(max_length=100)


class Questions(models.Model):
	subject = models.CharField(max_length=100)
	question = models.CharField(max_length=1000)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	answer = models.CharField(max_length=100)
    
    
    
    
    
    
    



 

