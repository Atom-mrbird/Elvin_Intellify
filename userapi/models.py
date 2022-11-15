from __future__ import absolute_import

from django.db import models
from django.contrib .auth.models import User
from django.utils import timezone
import os
from celery import Celery

class Warning(models.Model):
    name = models.CharField(blank=False,max_length=200)
    max_value = models.IntegerField(blank=False)
    datapoint_id = models.SlugField(blank=False, null=True, unique=True)
