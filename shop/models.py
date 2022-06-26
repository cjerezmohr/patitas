from django.db import models

# Create your models here.

class Pet_food(models.Model):
    name = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.FloatField()

class Pet_toys(models.Model):
    name = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.FloatField()

class Pet_vet(models.Model):
    name = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.FloatField()

