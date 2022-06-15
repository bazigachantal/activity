from re import M
from django.db import models

# Create your models here.

class Bursary(models.Model):
    header = models.CharField(max_length=150)
    expiain = models.TextField()
    technology = models.CharField(max_length=200)
    pub_date = models.DateTimeField('now')
    outhor = models.CharField(max_length=50)

