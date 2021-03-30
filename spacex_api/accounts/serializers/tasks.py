"""Tasks serializers."""

# Django
from django.utils.translation import gettext_lazy as _

# Rest Framework
from rest_framework import serializers

# Models
from spacex_api.accounts.models.tasks import Task
from spacex_api.accounts.models.base import Status

# Services
from spacex_api.utils.services.trello.cards import create_card


class TaskSerializer(serializers.ModelSerializer):
    """Task model serializer.
    ---
    This class run all the logic behind the http request
    for sending the tasks to Trello.
    """
    status_id = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Status.objects.all(),
        required=True,
        error_messages={
            'does_not_exist': _('Object with {slug_name}={value} does not exist. Valid options are %s' % str(Status.get_names_list())),
        }
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created', 'modified',)
        extra_kwargs = {'trello_list': {'required': True}}

    # def validate(self, attrs):
    #     """Validate.
    #     ---
    #     """
        

    def create(self, validated_data):
        """Create method.
        ---
        1. Send information to Trello.
        2. Save information in the database.
        """
        instance = super().create(validated_data)
        # create_card(
        #     task=instance
        # )

        return instance