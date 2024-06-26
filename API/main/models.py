from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    turf_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    teammates_count = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
