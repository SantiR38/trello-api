"""Tasks models."""

# Django
from django.db import models

# Models
from spacex_api.accounts.models.base import BaseModel
from spacex_api.accounts.models.categories import Category
from spacex_api.users.models import User


class Task(BaseModel):
    """Task model.
    ---
    This is the model that will save in the database all the tasks sended to Trello."""

    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    trello_list = models.CharField(max_length=140, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
