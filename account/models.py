from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='Name', max_length=5)
    sex = models.CharField(verbose_name='Sex', default='Male', max_length=10)
    phone = models.CharField(verbose_name='Phone Number', max_length=11)
    login_count = models.IntegerField(verbose_name='Login Times', default=1)
    type = models.IntegerField(verbose_name='User type', default=1)
    create_date = models.DateField(verbose_name='register date', default=timezone.now)
    update_date = models.DateTimeField(verbose_name='Update date', auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['-id']
        managed = True
        db_table = 'userprofile'
        verbose_name = "Info"