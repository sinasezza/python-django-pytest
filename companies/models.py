from django.db import models
from django.utils import timezone


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        max_length=20, choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=timezone.now, editable=True)
    application_link = models.URLField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
