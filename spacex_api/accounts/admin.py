"""Accounts models admin."""

# Django
from django.contrib import admin

# Models
from spacex_api.accounts.models import base, categories


@admin.register(base.Status)
class StatusAdmin(admin.ModelAdmin):
    """Status model admin."""

    list_display = ('id', 'name',)

@admin.register(categories.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category model admin."""

    list_display = ('id', 'name',)
