from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    reporter = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    location_lat = models.FloatField(null=True, blank=True)
    location_lng = models.FloatField(null=True, blank=True)
    is_anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='New')
    assigned_counselor = models.ForeignKey(User, null=True, blank=True, related_name='assigned_reports', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
