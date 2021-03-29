"""Exception classes."""

# Rest Framework
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework import status


def base_exception_handler(exc, context):
    """ Base exception handler function.
    Call DRF's default exception handler first,
    to get the standard error response."""

    response = exception_handler(exc, context)

    # check that a ValidationError exception is raised
    if isinstance(exc, ValidationError):
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        response.data['status_code'] = response.status_code

    return response