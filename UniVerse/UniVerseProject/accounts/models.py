from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student_registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    rollnumber=models.IntegerField(null=True,unique=True)
    enrollment=models.IntegerField(null=True,unique=True)
    course=models.CharField(max_length=20,null=True)
    mobile=models.IntegerField(null=True)
    admission_year=models.IntegerField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)
    

    def __str__(self):
        return f"{self.user}"
