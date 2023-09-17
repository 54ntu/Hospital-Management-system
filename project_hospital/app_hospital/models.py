from django.db import models

# Create your models here.
class patientModel(models.Model):
    firstname = models.CharField(max_length=100,null=False,blank=False)
    lastname = models.CharField(max_length=100,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    sex = models.CharField(max_length=50, null=False,blank=False)


    def __str__(self):
        return self.firstname
    
