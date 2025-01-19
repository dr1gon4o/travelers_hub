from django.db import models
from traveler.models import Traveler
from django.core.exceptions import ValidationError


def validate_destination(value):
    """
    Validates the destination field to ensure it has a length between 3 and 100 characters.
    """
    if not (3 <= len(value) <= 100):
        raise ValidationError("Destination must be between 3 and 100 characters.")


class Trip(models.Model):
    destination = models.CharField(max_length=100, blank=False, null=False, validators=[validate_destination])
    summary = models.TextField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    duration = models.PositiveSmallIntegerField(default=1, help_text="*Duration in days is expected.", blank=False, null=False)
    image_url = models.URLField(blank=True, null=True)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name="trips")

    def __str__(self):
        return self.destination
