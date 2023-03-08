from django.conf import settings
from django.db import models

from trackerauth.models import ArchiveModel


class Baby(ArchiveModel):
    FEMALE = "f"
    MALE = "m"

    GENDER_CHOICES = (
        (FEMALE, "Female"),
        (MALE, "Male")
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="babies")
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateTimeField()
    time_of_birth = models.TimeField()
    due_day = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Babies"

    def __str__(self):
        """Return a human-readable string representing a record"""
        return f'{self.name} ({self.get_gender_display()})'
