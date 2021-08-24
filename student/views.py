from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.

from student.models import Result
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings 
from django.core.mail import send_mail 
import json
import os
import datetime
from tkinter import *
from django.contrib.auth.decorators import login_required
from quiz.models import CreateQuiz,Questions
from django.core.paginator import Paginator

lst = []
answers = Questions.objects.all()
anslist = []
for i in answers:
	anslist.append(i.answer)       
                         
# Create your views here.
def index(request):
	obj = Questions.objects.all()
	count = Questions.objects.all().count()

	paginator = Paginator(obj,1)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page =1

	try:
		questions = paginator.page(page)
	except(EmptyPage,InvalidPage):
		questions=paginator.page(paginator.num_pages)
	return render(request,'student/index.html',{'obj':obj,'questions':questions,'count':count})
    
            
def studentlogin(request):
	if request.method =="POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			check = CreateQuiz.objects.get(email=email, dob=password)
			request.session['userid'] = check.id
                       
			return redirect('start')
		except:
			pass

	return render(request,'student/studentlogin.html') 


   

def save_ans(request):
            ans = request.GET['ans']
            lst.append(ans)

def start(request):
		lst.clear()
		now = datetime.datetime.now().strftime('%H:%M:%S')
		return render(request,'student/start.html')


def result(request):
            score =0
            for i in range(len(lst)):
                if lst[i]==anslist[i]:
                    score +=1
            now2 = datetime.datetime.now().strftime('%H:%M:%S')
                      
            name = request.session['userid']
            opj = CreateQuiz.objects.get(id=name)
            num = opj.studentname
            Result.objects.create(id=name,name=num,endtime=now2,score=score)
            return render(request,'student/result.html',{'score':score,'lst':lst,'now2':now2,'form':opj})


        
            
    