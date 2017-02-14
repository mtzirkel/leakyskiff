from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Overarching quz class


class Quiz(models.Model):

    title = models.CharField(
        verbose_name=('Title'),
        max_length=60,
        blank=False)

    created_by = models.ForeignKey(User,
                                   verbose_name=('Created by:'),
                                   blank=False)

    created_date = models.DateField(auto_now_add=True,
                                    verbose_name=('Date Created:'))

    def __unicode__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=400)
    point_value = models.IntegerField(default=1)
    inquiz = models.ForeignKey(Quiz)
    #figure = models.ImageField()

    def __unicode__(self):
        return self.question_text


class Answer(models.Model):
    to_question = models.ForeignKey(Question)
