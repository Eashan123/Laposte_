class BaseError(Exception):
    """Base package error."""


class InvalidModelInputError(BaseError):
    """Model input contains an error."""

# This are some of the python best practices, check preprocessors regex function.