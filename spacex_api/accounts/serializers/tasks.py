"""Tasks serializers."""

# Python Libraries
from random import random
from math import floor
from random_word import RandomWords

# Django
from django.utils.translation import gettext_lazy as _

# Rest Framework
from rest_framework import serializers

# Services
from spacex_api.utils.services.trello.cards import create_card
from spacex_api.utils.services.trello.boards import get_a_board


class TaskSerializer(serializers.Serializer):
    """Task serializer.
    ---
    This class run all the logic behind the http request
    for sending the tasks to Trello.
    """
    name  = serializers.CharField(required=False)
    desc = serializers.CharField(required=False)
    category = serializers.CharField(required=False)

    def validate(self, attrs):
        """Validate.
        ---
        1. Get user instance from request.
        2. Get Board.
        3. Validate categories.
            3.1 Get board labels
            3.2 Set labels as category choices
        4. Get id of board members.
        5. Get board ToDo list.
        6. If category == "Bug":
            6.1. Autogenerate name.
            6.2. A random member is assigned to a "Bug" task.
        7. Categories become idLabels.
        """
        # 1. Get user instance from request.
        request = self.context.get("request")
        if request and hasattr(request, "user") and request.method == "POST":
            attrs['user_id'] = request.user

        # 2. Get Board
        board = get_a_board(user=request.user)

        # 3. Validate categories.
        # 3.1 Get board labels
        category_choices = [i["name"] for i in board["labels"]]
        # 3.2 Set labels as category choices
        if attrs["category"] not in category_choices:
            raise serializers.ValidationError({"detail": f"{attrs['category']} is not a valid option. Valid options are: {str(category_choices)}"})

        # 4. Get id of board members
        members_ids = [i["id"] for i in board["members"]]

        # 5. Get board ToDo list.
        lists_id = [i for i in board["lists"]]
        attrs["idList"] = list(filter(lambda x: x["name"] == "To Do", lists_id))[0]["id"]

        # 6. If category == "Bug":
        if attrs["category"] == "Bug":
            # 6.1. Autogenerate name.
            attrs["name"] = f"Bug-{RandomWords().get_random_word()}-{floor(random()*100000 + 1)}"
            # 6.2. A random member will be assigned to a "Bug" task.
            attrs["idMembers"] = [members_ids[floor(random()*len(members_ids))]]

        # 7. Categories become idLabels.
        labels = list(filter(lambda x: x["name"]==attrs["category"], board["labels"]))
        attrs["idLabels"] = list(map(lambda x: x["id"], labels))
        attrs.pop("category")

        return attrs
        

    def create(self, validated_data):
        """Create method.
        ---
        Send information to Trello cards.
        """
        response = create_card(**validated_data)
        print(response.status_code)

        return response

    # Card attrs
    
    # name
    # desc
    # idList (req)
    # idMembers ["member_1", "member_2"]
    # idLabels  ["label_1", "label_2"]