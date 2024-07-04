from django.db import models
from datetime import datetime
from django.contrib.auth.models import Group


class predict(models.Model):
   fname = models.CharField(max_length=40)
   sname = models.CharField(max_length=40)
   email = models.EmailField(max_length=90)
   HbA1c_level = models.IntegerField()
   blood_glucose_level = models.IntegerField()
   age = models.IntegerField()
   bmi = models.IntegerField()
   hypertension = models.IntegerField()
   results = models.CharField(null=True, max_length=20)
   date_Time = models.DateTimeField(default=datetime.now)
  
   
   def __str__(self):
      return self.fname +  ' ' + self.sname
   
   
   
class RF_model(models.Model):
   
   fname = models.CharField(max_length=40)
   sname = models.CharField(max_length=40)
   email = models.EmailField(max_length=90)
   HbA1c_level = models.FloatField()
   blood_glucose_level = models.IntegerField()
   age = models.IntegerField()
   bmi = models.FloatField()
   hypertension = models.IntegerField()
   RF_predicted = models.CharField(null=True, max_length=20)
   RF_prob = models.CharField(null=True, max_length=100)
   date_Time = models.DateTimeField(default=datetime.now)
   
   
   def __str__(self):
      return self.fname + ' ' + self.sname
   
   
   
   
   
   
class interaction(models.Model): 
   
   clicked = models.IntegerField()
   onload = models.IntegerField()
   
   
   

   
