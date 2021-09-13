from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.

from quiz.models import SignUp,CreateQuiz,Questions
from django.views.decorators.csrf import csrf_exempt
from student.models import Result
from django.http import JsonResponse
from django.conf import settings 
from django.core.mail import send_mail 
import json
import os
from tkinter import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    
        data = {"success": False}
        if request.method =="POST":
            institutionname = request.POST.get('institutionname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            mobilenumber = request.POST.get('mobilenumber')
            address = request.POST.get('address')
            principalname = request.POST.get('principalname')
            principalno = request.POST.get('principalno')
            los = request.POST.get('los')
            if SignUp.objects.filter(email= email).exists():
                messages.info(request,'Email Already Exists !!!')
                return redirect('signup')

            else:       
                SignUp.objects.create(institutionname=institutionname, email=email,password= password, mobilenumber=mobilenumber,address=address,principalname=principalname,principalno=principalno, los=los )
                return render(request,'quiz/signup.html')

        return render(request,'quiz/signup.html')



def login(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            check = SignUp.objects.get(email=email, password=password)
            request.session['userid'] = check.id
            return redirect('dash')
        except:
            pass
    return render(request,'quiz/login.html')

      
    	

def createquiz(request):
    data = {"success": False}
    if request.method =="POST":
        studentname = request.POST.get('studentname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        std = request.POST.get('std')  
        gender= request.POST.get('gender')  

        CreateQuiz.objects.create(studentname=studentname,dob=dob,email=email, subject=subject,std=std,gender=gender)
        subject = 'TEST GURU QUIZ'
        message = f'Hi {studentname}, \n\n  Thank you for registering in Test Guru.\n\n  Your quiz was ready\n\n\t\t Username : {email} \n\n\t\t Password : {dob}\n\n   \t All the best... '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

    return render(request,'quiz/createquiz.html')  	      
         
  


		

def results(request):
    obj = Result.objects.all()
    return render(request,'quiz/results.html',{'objects':obj})


def questions(request):
	data = {"success": False}
	if request.method =="POST":
		subject = request.POST.get('subject')
		question = request.POST.get('question')
		option1 = request.POST.get('option1')
		option2 = request.POST.get('option2')
		option3 = request.POST.get('option3')
		option4 = request.POST.get('option4')
		answer = request.POST.get('answer')

		Questions.objects.create(subject=subject,question=question,option1=option1, option2=option2,option3=option3,option4=option4,answer=answer)

	return render(request, 'quiz/questions.html')    
        



def dash(request):
    data = {"success": False}
    if request.POST.get('create') == "create":
        return render(request, 'quiz/createquiz.html')
    if request.POST.get('results') == "results":
        return redirect('results')
    if request.POST.get('creque') == "creque":
        return render(request, 'quiz/questions.html')
    return render(request, 'quiz/dash.html')


def logout(request):
    return redirect('login')
        
        
        
        
        
        

        

    

        
        
        
          
        
          

        

	
    