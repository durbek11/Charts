from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

class MyUser(models.Model):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

class ContactUs(models.Model):
    TAKLIF = "Taklif"
    SHIKOYAT = "Shikoyat"
    CONTACT_CHOICES = [
        (TAKLIF, "Taklif"),
        (SHIKOYAT, "Shikoyat")
    ]
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=TAKLIF)
    message = models.TextField(max_length=700)
    is_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}, subject: {self.subject}"

