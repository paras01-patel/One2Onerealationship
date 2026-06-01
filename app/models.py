from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Adharcard(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    adharno = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.adharno