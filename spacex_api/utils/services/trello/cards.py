"""Trello cards services."""

# Libraries
import requests

# Services
from spacex_api.utils.services.trello.base import perform_request

def create_card(**kwargs):
   """Create card.
   ---
   This function is called by the create method in serializer
   after saving an instance of task.
   The instance data is sended to Trello, and saved as a card.
   """
   url = "https://api.trello.com/1/cards"
   user = kwargs.pop("user_id")
   print(kwargs)
   response = perform_request(
      method="POST",
      url=url,
      query=kwargs,
      user=user
    )
   print(f"Create card status: {response.status_code}")
   print(response.json())
   return response
   