# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def _str_(self):

