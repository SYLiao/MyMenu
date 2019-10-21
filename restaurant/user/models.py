from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):

    user = models.OneToOneField(User, models.CASCADE, related_name='profile')

    username = models.CharField('username', max_length=50, blank=True)

    cellPhoneNumber = models.CharField('cellphone', max_length=20, blank=True)

    modifyDate = models.DateTimeField('Date', auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return str(self.user)
