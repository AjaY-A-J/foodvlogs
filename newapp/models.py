# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class food(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='foods')
    desc=models.TextField()
    price=models.IntegerField()