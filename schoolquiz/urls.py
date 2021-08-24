"""schoolquiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from schoolquiz import settings
from quiz import views as quiz_views
from student import views as student_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),

url(r'^$',quiz_views.login, name="login"),
url(r'^signup$',quiz_views.signup, name="signup"),
url(r'^dash',quiz_views.dash, name="dash"),
url(r'^createquiz',quiz_views.createquiz, name="createquiz"),
url(r'^questions',quiz_views.questions, name="questions"),
url(r'^results',quiz_views.results, name="results"),

url(r'^studentlogin', student_views.studentlogin, name="studentlogin"),
url(r'^start', student_views.start, name="start"),
url(r'^index', student_views.index, name="index"),
url(r'^save_ans', student_views.save_ans,name="saveans"),
url(r'^result', student_views.result, name="result"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






