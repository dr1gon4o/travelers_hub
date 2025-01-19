from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_nickname(value):
    if not re.match(r'^[a-zA-Z0-9]{3,30}$', value):
        raise ValidationError("Your nickname is invalid!")


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_nickname],
        help_text="*Nicknames can contain only letters and digits."
    )
    email = models.EmailField(max_length=30,  blank=False, null=False, unique=True)
    country = models.CharField(max_length=3, blank=False, null=False)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname

    # def __str__(self):
    #     return f"{self.destination} - {self.start_date}"


    # def save(self, *args, **kwargs):
    #     # Check if a User with the same nickname exists
    #     user, created = User.objects.get_or_create(username=self.nickname)
    #
    #     # Update the User's email if it's different
    #     if user.email != self.email:
    #         user.email = self.email
    #         user.save()
    #
    #     super().save(*args, **kwargs)