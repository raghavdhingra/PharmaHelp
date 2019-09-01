from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.postgres.fields import JSONField , ArrayField ,DateTimeRangeField

# Create your models here.
class Labs(models.Model):
    name = models.TextField(default="",null=True,blank=True)
    location = models.CharField(max_length=500,blank=True,null=True,default='')
    contact = models.TextField(blank=True,null=True,default='9876543210')
    rating = models.IntegerField(blank=True,null=True,default=0)
    test = models.TextField(blank=True,null=True,default='')
    timing = models.TimeField(default=timezone.now)
    availability = models.BooleanField(default=True)
    certified = models.BooleanField(default=False)
    description = models.TextField(null=True,blank=True,default='')
    joined_on = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0,null=True,blank=True)

    def publish(self):
        self.joined_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name