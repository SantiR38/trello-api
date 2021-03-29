"""Accounts app config."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    name = "spacex_api.accounts"
    verbose_name = _("Accounts")
