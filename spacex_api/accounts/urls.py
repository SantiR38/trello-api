"""Accounts urls."""

# Django
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from spacex_api.accounts.views import tasks, boards

router = DefaultRouter()
router.register(r'tasks', tasks.TaskViewset, basename='tasks')

app_name = "accounts"
urlpatterns = [
    path('', include(router.urls)),
    path("boards/", view=boards.ListBoardsView.as_view(), name="update"),
]
