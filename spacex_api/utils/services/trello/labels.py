"""Trello Labels services."""

# Python Libraries
import requests

# Services
from .base import get_needed_data, perform_request


def create_label(user=None, name=None, color=None, board_id=None):
    """Create label function."""
    url = "https://api.trello.com/1/labels"

    query = {
        'name': name,
        'color': color,
        'idBoard': board_id
    }
    response = perform_request(
        method="POST",
        url=url,
        query=query,
        user=user
    )
    return response