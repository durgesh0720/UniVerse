from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class admin_registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    id_number=models.IntegerField(primary_key=True)
    mobile=models.CharField(max_length=15,null=True)
    

    def __str__(self):
        return f"{self.id_number}"
