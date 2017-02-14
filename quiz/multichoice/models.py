from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from quiz.models import Quiz, Question, Answer




# The is the question model for multiple choice question
class MCQuestion(Question):
    answer_a = models.CharField(max_length=200, default="Empty")#label = "A."
    a_is_correct = models.BooleanField(default=False)#
    answer_b = models.CharField(max_length=200, default="Empty")#label = "B.")
    b_is_correct = models.BooleanField(default=False)#label = "Is B. the correct answer?", required = False)
    answer_c = models.CharField(max_length=200, default="Empty")#label = "C.")
    c_is_correct = models.BooleanField(default=False)#label = "Is C. the correct answer?", required = False)
    answer_d = models.CharField(max_length=200, default="Empty")#label = "D.")
    d_is_correct = models.BooleanField(default=False)#label = "Is D. the correct answer?", required = False)



class MCAnswer(Answer):
	student_choices = models.ForeignKey(MCQuestion, 
		blank = False, 
		null = False, 
		limit_choices_to={'a_is_correct', 'b_is_correct', 'c_is_correct', 'd_is_correct'})
	