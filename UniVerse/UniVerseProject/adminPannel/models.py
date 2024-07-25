from django.db import models

# Create your models here.

class admin_registration(models.Model):
    id_number=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=15,null=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id_number}"