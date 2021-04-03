"""Trello lists services."""

# Python Libraries
import requests

# Services
from .base import get_needed_data

def get_lists(user=None, board_id=None):
    """Get boards
    ---
    Make a list with all the trello boards.
    """
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    response = perform_request(
        method="GET",
        url=url,
        user=user
    )
    board_lists = list(map(get_needed_data, response.json()))
    return board_lists