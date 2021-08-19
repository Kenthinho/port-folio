from django.core.mail import message
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
