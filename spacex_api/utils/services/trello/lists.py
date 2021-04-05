"""Trello lists services."""

# Python Libraries
import requests

# Services
from spacex_api.utils.services.trello.base import get_needed_data, perform_request

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
    print(f"Get lists status: {response.status_code}")
    board_lists = list(map(get_needed_data, response.json()))
    return board_lists