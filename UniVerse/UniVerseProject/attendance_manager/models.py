from django.db import models
from accounts.models import student_registration #type:ignore
from django.core.validators import MinValueValidator,MaxValueValidator

class AttendanceYear(models.Model):
    user = models.ForeignKey(student_registration, on_delete=models.CASCADE,null=True,blank=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2018)], null=True)

    def __str__(self):
        return f"{self.user} - {self.year}"

class AttendanceMonth(models.Model):
    attendance_year = models.ForeignKey(AttendanceYear, on_delete=models.CASCADE)
    month = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(12)],null=True)
    present_days = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)], null=True)

    def __str__(self):
        return f"{self.attendance_year.year} - {self.month}: {self.present_days} days"
    
    def get_month_display(self):
        month_names = {
            1: "January", 2: "February", 3: "March", 4: "April",
            5: "May", 6: "June", 7: "July", 8: "August",
            9: "September", 10: "October", 11: "November", 12: "December"
        }
        return month_names.get(self.month, "Unknown")