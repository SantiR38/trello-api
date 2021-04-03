"""Base Trello functions."""

# Python Libraries
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

def perform_request(method="GET", query=dict(), user=None, url=None):
    """Perform request Trello function."""
    query["key"] = user.trello_key
    query["token"] = user.trello_token
    response = requests.request("POST", url, params=query)
    return response