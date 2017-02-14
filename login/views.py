from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.models import User, Group

 

@login_required
def home(request):
	if request.user.groups.filter(name='teacher'):
		return render(request, 'teacher_home.html')
	elif request.user.groups.filter(name='student'):
		return render(request, 'student_home.html')
	else:
		return render(request, 'superuser_home.html')	
	