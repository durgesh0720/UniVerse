from django.db import models

# Create your models here.
class student_registration(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
