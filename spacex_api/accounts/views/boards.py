"""Boards views."""

# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Services
from spacex_api.utils.services.trello.boards import get_boards

class ListBoardsView(APIView):
    """List Boards view."""

    def get(self, request, format=None):
            data = get_boards(request.user)
            return Response(data)
    