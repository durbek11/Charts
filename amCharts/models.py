from audioop import add
from django.db import models
from django.contrib.auth.models import AbstractUser


class Chart(models.Model):
    PIE = "Pie"
    COLUMN = "Column"
    CHART_CHOICES = [
        (PIE, "Pie Chart"),
        (COLUMN, "Column Chart")
    ]
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name='chart' )
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    caption = models.TextField(max_length=700)
    created_on = models.DateTimeField(("date joined"), default=timezone.now)
    chart_type = models.CharField(max_length=15,choices=CHART_CHOICES, default=PIE)
    def __str__(self):
        return self.name

