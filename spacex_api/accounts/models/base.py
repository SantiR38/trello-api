"""Abstract models."""

# Django
from django.db import models

# Mixins
from spacex_api.utils.mixins.models import NamesListingModelMixin

class Status(NamesListingModelMixin, models.Model):
    """Status model."""
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name_plural = "status"

    def __str__(self):
        return self.name
