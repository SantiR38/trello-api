"""Sign up views."""

# Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Serializers
from spacex_api.users.serializers.sign_up import SignUpSerializer


class SignUpView(CreateAPIView):
    """Sign Up View."""

    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)