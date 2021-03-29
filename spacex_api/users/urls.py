"""Users urls."""

# Django
from django.urls import path


# Views
from spacex_api.users.views.default import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
from spacex_api.users.views import sign_up


app_name = "users"
urlpatterns = [
    path('sign-up/', sign_up.SignUpView.as_view(), name='sign_up'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
