"""Trello cards services."""

# Libraries
import requests

def create_card_data(task):
   """Create card data.
   ---
   This function is called bay `create_card()`.
   It only creates the json data so `create_card()`
   can send the information to Trello.
   """


def create_card(**kwargs):
   """Create card.
   ---
   This function is called by the create method in serializer
   after saving an instance of task.
   The instance data is sended to Trello, and saved as a card.
   """
   data = create_card_data(task)
   url = "https://api.trello.com/1/cards"
   user = kwargs["user_id"]
   query = {
      'idList': "",
      "name": "",
      "desc": ""
   }
   response = perform_request(
      method="POST",
      url=url,
      query=query,
      user=user
    )
   return response
   