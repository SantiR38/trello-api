"""User models."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for spacex_api."""

    first_name = models.CharField(_("First name of User"), max_length=140, null=True)
    last_name = models.CharField(_("Last name of User"), max_length=140, null=True)
    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    trello_key = models.CharField(max_length=140, null=True)
    trello_token = models.CharField(max_length=255, null=True)
    trello_board_id = models.CharField(max_length=140, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.email

