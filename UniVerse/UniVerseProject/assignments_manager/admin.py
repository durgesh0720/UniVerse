from django.contrib import admin
from .models import AssignmentDetails,UserDetails,UserSubmission
# Register your models here.
admin.site.register(AssignmentDetails)
admin.site.register(UserDetails)
admin.site.register(UserSubmission)

