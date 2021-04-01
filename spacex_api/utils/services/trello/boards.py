"""Trello Boards services."""

import requests

def get_needed_data(element):
    """Get needed data
    ---
    Gets all the data from the api response
    and returns it sintetized.
    """
    data = {
        "id": element["id"],
        "name": element["name"]
    }
    if "url" in element:
        data["url"] = element["url"]
    return data

# --------- LISTS ---------- #

def get_lists(user=None, board_id=None):
    """Get boards
    ---
    Make a list with all the trello boards.
    """
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    query = {
        'key': user.trello_key,
        'token': user.trello_token
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    board_lists = list(map(get_needed_data, response.json()))
    return board_lists


# --------- BOARDS ---------- #

def get_boards(user=None):
    """Get boards
    ---
    Make a list with all the trello boards.
    """
    url = f"https://api.trello.com/1/members/{user.trello_username}/boards"
    query = {
        'key': user.trello_key,
        'token': user.trello_token
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    boards = list(map(get_needed_data, response.json()))
    for board in boards:
        board["lists"] = get_lists(user=user, board_id=board["id"])
    return boards






# def consume_global_pay_api(
#         context=None,
#         url=None,
#         app_code=env("SERVER_APP_CODE"),
#         app_key=env("SERVER_APP_KEY"),
#         http_method="POST",
#         params=None
#     ):
#     """Make payment function."""
    
#     headers = {'Auth-Token': auth.get_token(
#         app_code=app_code,
#         app_key=app_key
#     )}


#     r = None
#     if http_method == "POST":
#         r = requests.post(
#             url,
#             data=json.dumps(context, default=decimal_default),
#             headers=headers
#         )
#     elif http_method == "GET":
#         r = requests.get(url, params=params, headers=headers)
#     return r