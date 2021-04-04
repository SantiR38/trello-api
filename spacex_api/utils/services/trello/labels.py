"""Trello Labels services."""

# Python Libraries
import requests

# Services
from spacex_api.utils.services.trello.base import get_needed_data, perform_request


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
    print(f"Create label status: {response.status_code}")
    return response

def get_labels(user=None):
    """Get labels from a board."""
    url = f"https://api.trello.com/1/boards/{user.trello_board_id}/labels"
    response = perform_request(
        method="GET",
        url=url,
        user=user
    )
    print(f"Get labels status: {response.status_code}")
    response = list(map(get_needed_data, response.json()))
    return response