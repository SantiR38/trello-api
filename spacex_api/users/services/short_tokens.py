"""Services for handling short tokens."""

# Python libraries
import string
import secrets

# Models
from spacex_api.users.models import ShortToken

def create_token():
    """Create token function.

    Creates an alphanumeric 6 characters token.
    """
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for i in range(6))
    return token

def short_token_is_valid(email, short_token):
    """Short token is valid function.

    Validate if:
    1. ShortToken instance exists.
    2. Token matchs with email in ShortToken instance.
    """
    instance = ShortToken.objects.filter(user_email=email)
    if not instance.exists() or not instance[0].verify_token(short_token):
        return False
    return True