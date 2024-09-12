from django.db import models
# Create your models here.
class CustomerForm(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    complaint = models.CharField(max_length=255,null=True, blank=True)