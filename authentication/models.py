from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(blank=False,max_length=200)
    Item2 = models.TextField(blank=False,max_length=200)
    Item3 = models.TextField(blank=False,max_length=200)

class Datasource(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(auto_created=True,max_length=200)

class Datapoint(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    datasource_id = models.CharField(auto_created=True,max_length=200)

class Telemdata(models.Model):
    value = models.ForeignKey(Datasource, on_delete=models.CASCADE)
    datapoint_id = models.ForeignKey(Datapoint, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)