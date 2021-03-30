"""Tasks views."""

# Rest Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

# Serializers
from spacex_api.accounts.serializers.tasks import TaskSerializer


class TaskViewset(CreateModelMixin, GenericViewSet):
    """Task viewset.
    ---
    Only avaliable `create()` method.
    """
    serializer_class = TaskSerializer
