"""Categories models."""

# Django
from django.db import models

# Models
from spacex_api.accounts.models.base import BaseModel

class Category(BaseModel):
    """Category class."""
    name = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
