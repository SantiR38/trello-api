"""Sign up serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from spacex_api.users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    """Sign Up serializer.
    ------
    Used for signing up users.
    """

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',]
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}}

    def create(self, validated_data):
        """
        User create method.
        ---
        Creates User and TypeServiceUser(all in 0) instances.
        """
        # User
        password = validated_data.pop('password')
        user = User(**validated_data, username=validated_data['email'])
        user.set_password(password)
        user.save()

        return user
