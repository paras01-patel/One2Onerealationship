from django.db import models

# Create your models here.


class Person(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Adharcard(models.Model):
    person=models.OneToOneField(Person,on_delete=models.CASCADE)
    adharno=models.CharField( max_length=50)
    
    def __str__(self):
        return self.adharno