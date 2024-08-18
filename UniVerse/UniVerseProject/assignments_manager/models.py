from django.db import models
from adminPannel.models import admin_registration #type:ignore
# Create your models here.
class AssignmentDetails(models.Model):
    assignment_number=models.IntegerField()
    unit_title=models.CharField(max_length=50,blank=True)
    className=models.CharField(max_length=20,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField()
    questions=models.TextField()
    submit_by=models.CharField(max_length=20,blank=True)
    unit_number=models.IntegerField(blank=True, null=True)
    subject_name=models.CharField(max_length=50,blank=True)
    semester=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.assignment_number} {self.unit_title} {self.due_date}"
    admin_user = models.ForeignKey(admin_registration, related_name='assignments', on_delete=models.SET_NULL, null=True, blank=True)


class UserDetails(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    roll_number=models.IntegerField(primary_key=True)
    _class=models.CharField(max_length=20)
    semester=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.roll_number} {self._class}"
    
class UserSubmission(models.Model):
    user=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    assignment_file = models.FileField(upload_to='assignment_File/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,blank=True)
    assignmentid=models.IntegerField(null=True)
    massage=models.TextField(blank=True)
    def __str__(self):
        return f"{self.pk} {self.user.roll_number}"
    

