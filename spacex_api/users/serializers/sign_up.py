"""Sign up serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from spacex_api.users.models import User

# Services
from spacex_api.utils.services.trello.boards import create_board

class SignUpSerializer(serializers.ModelSerializer):
    """Sign Up serializer.
    ------
    Used for signing up users.
    """

    class Meta:
        error_messages = {'required': 'This field is required. Go to https://trello.com/app-key to get this value.'}
        model = User
        fields = [
            'trello_key',
            'trello_token',
            'trello_username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'trello_key': {'required': True, 'error_messages': error_messages},
            'trello_token': {'required': True, 'error_messages': error_messages},
            'trello_username': {'required': True}
        }

    def create(self, validated_data):
        """
        User create method.
        ---
        Creates User instances.
        """
        # User
        password = validated_data.pop('password')
        user = User(**validated_data, username=validated_data['email'])
        user.set_password(password)
        response = create_board(user=user)
        if response.status_code == 200:
            user.trello_board_id = response.json()["id"]
        user.save()
        return user

    def to_representation(self, instance):
        """Set country_id to string."""
        ret = super().to_representation(instance)
        if instance.trello_board_id is None:
            ret["error"] = {"Error": "The Trello board was not created."}
        return ret

