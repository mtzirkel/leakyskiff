from django.forms import ModelForm
from django import forms
from models import Quiz, Question



class NewQuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']


class NewQuestionForm(ModelForm):
	class Meta:
		model = Question   
		fields ='__all__'     

    
