"""Trello Boards services."""

# Python Libraries
import requests

# Services
from .base import get_needed_data, perform_request
from .lists import get_lists
from .labels import create_label


def create_board(user=None):
    """Create a board."""
    url = f"https://api.trello.com/1/boards/"
    query = {
        'name': "Space-X tasks"
    }
    response = perform_request(
        method="POST",
        url=url,
        query=query,
        user=user
    )
    if response.status_code == 200:
        data = {
            "red": "Maintenance",
            "blue": "Research",
            "green": "Test"
        }
        for key, value in data.items():
            create_label(user=user, color=key, name=value, board_id=response.json()["id"])
    return response
    

def get_boards(user=None):
    """Get boards
    ---
    Make a list with all the trello boards.
    """
    url = f"https://api.trello.com/1/members/{user.trello_username}/boards"
    response = perform_request(
        method="GET",
        url=url,
        user=user
    )
    boards = list(map(get_needed_data, response.json()))
    for board in boards:
        board["lists"] = get_lists(user=user, board_id=board["id"])
    return boards
