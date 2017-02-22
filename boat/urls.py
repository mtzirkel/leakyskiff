"""boat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from login import views as login_views
from quiz import views as quiz_views
from quiz.multichoice import views as multichoice_views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
    url(r'^home/$', login_views.home),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', quiz_views.add_quiz),
    url(r'^quiz/$', login_views.home),
    url(r'^quizlist/$', quiz_views.teacher_quizlist),
    url(r'^squizlist/$', quiz_views.student_quizlist),
    url(r'^(?P<quiz_id>\d+)/add_question/$', multichoice_views.add_mcquestion),#old not as good way to add question
    url(r'^quizquestions/(?P<quiz_id>\d+)/$', quiz_views.question_list, name='question-list'),#new way to add question
    url(r'^quizquestions/(?P<quiz_id>\d+)/questioncreate/$', quiz_views.question_create, name='question-create'), #new way to add question
    url(r'^quizquestions/(?P<quiz_id>\d+)/question/(?P<pk>[0-9]+)/update/$', quiz_views.question_update, name='question-update'),
]


