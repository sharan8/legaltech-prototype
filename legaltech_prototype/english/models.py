from django.db import models

# Create your models here.


class Problem(models.Model):
    name = models.CharField(max_length=100)
    coa = models.CharField(max_length=100)