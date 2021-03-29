"""Abstract models."""

# Django
from django.db import models

class Status(models.Model):
    """Status model."""
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name_plural = "status"

    def __str__(self):
        return self.name

class BaseModel(models.Model):
    """BaseModel.
    ---
    It has the common info for all the models.
    So models don't inherit from models.Model, but from this class.
    """
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
