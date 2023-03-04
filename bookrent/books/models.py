from django.db import models

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=100)
    quantity =  models.IntegerField()
    description =  models.TextField()


class students(models.Model):
    bookname = models.CharField(max_length=100)
    netid = models.CharField(max_length=100)