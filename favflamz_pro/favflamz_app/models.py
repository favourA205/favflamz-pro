from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class RegistrationData(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.username)


class Select(models.Model):
    subject = models.CharField(max_length=150)
    years = models.CharField(max_length=10)


    def __str__(self):
        return '{}'.format(self.subject)


class signIn(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)

    def __str__(self):
        return '{}' .format(self.username)