from django.forms import ModelForm, Textarea, NumberInput, SelectMultiple
from django import forms
from .models import MCQuestion, MCAnswer


class MCQuestionForm(ModelForm):
    class Meta:
        model = MCQuestion
        fields = {'question_text',
                  'point_value',
                  'inquiz',
                  'answer_a',
                  'a_is_correct',
                  'answer_b',
                  'b_is_correct',
                  'answer_c',
                  'c_is_correct',
                  'answer_d',
                  'd_is_correct',
                  'inquiz'}

        widgets = {
            'question_text': Textarea(attrs={'cols': 70, 'rows': 10}),
            'point_value': NumberInput(attrs={'cols': 3, 'row': 1}),
            'answer_a': Textarea(attrs={'cols': 70, 'rows': 2}),
            'answer_b': Textarea(attrs={'cols': 70, 'rows': 2}),
            'answer_c': Textarea(attrs={'cols': 70, 'rows': 2}),
            'answer_d': Textarea(attrs={'cols': 70, 'rows': 2}),
        }


class MCAnswerForm(ModelForm):
    class Meta:
        model = MCAnswer
        fields = {'student_choices'}
        widgets = {'student_choice': SelectMultiple(choices='student_choices')}
