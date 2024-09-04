from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student_registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    rollnumber=models.IntegerField(null=True,unique=True)
    enrollment=models.IntegerField(null=True,unique=True)
    course=models.CharField(max_length=20,null=True)
    mobile=models.IntegerField(null=True)
    semester=models.IntegerField(null=True)
    bio=models.TextField(max_length=255,null=True)
    dob=models.DateField(null=True,blank=True,verbose_name="Date of Birth")
    address=models.TextField(null=True,blank=True)
    profession=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True,blank=True)

    def __str__(self):
        return f"{self.user}"

