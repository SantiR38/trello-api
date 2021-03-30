"""Categories models."""

# Django
from django.db import models

# Mixins
from spacex_api.utils.mixins.models import NamesListingModelMixin

# Models
from spacex_api.accounts.models.base import BaseModel

class Category(NamesListingModelMixin, BaseModel):
    """Category class."""
    name = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
