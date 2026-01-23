class AppException(Exception):
    """Base application exception"""
    retryable = True


class DuplicateOrderException(AppException):
    retryable = False