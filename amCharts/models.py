from audioop import add
from django.db import models
from django.contrib.auth.models import AbstractUser


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

