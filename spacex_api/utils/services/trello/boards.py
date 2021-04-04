"""Trello Boards services."""

# Python Libraries
import requests

# Services
from spacex_api.utils.services.trello.base import perform_request, get_needed_data
from spacex_api.utils.services.trello.lists import get_lists
from spacex_api.utils.services.trello.labels import create_label, get_labels


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
    print(f"Create board status: {response.status_code}")
    if response.status_code == 200:
        data = {
            "red": "Maintenance",
            "blue": "Research",
            "green": "Test",
            "purple": "Issue",
            "lime": "Bug"
        }
        for key, value in data.items():
            create_label(user=user, color=key, name=value, board_id=response.json()["id"])
    return response   
    

def get_boards(user=None):
    """Get boards
    ---
    Make a list with all the trello boards.
    """
    url = f"https://api.trello.com/1/members/me/boards"
    response = perform_request(
        method="GET",
        url=url,
        user=user
    )
    print(f"Get boards status: {response.status_code}")
    boards = list(map(get_needed_data, response.json()))
    for board in boards:
        board["lists"] = get_lists(user=user, board_id=board["id"])
    return boards


def get_a_board(user=None):
    
    url = f"https://api.trello.com/1/boards/{user.trello_board_id}"
    headers = {
    "Accept": "application/json"
    }
    response = perform_request(
        method="GET",
        url=url,
        headers=headers,
        user=user
    )
    print(f"Get a board status: {response.status_code}")
    if response.status_code == 200:
        response = get_needed_data(response.json())
        response["lists"] = get_lists(user=user, board_id=response["id"])
        response["labels"] = get_labels(user=user)
        response["members"] = perform_request(
            method="GET",
            url=f"https://api.trello.com/1/boards/{response['id']}/members",
            user=user
        ).json()
    return response