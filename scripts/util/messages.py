class Messages:
    # general

    MISSING_PARAMS = ''
    REQUEST_IS_NOT_A_JSON = 'Request is not a valid JSON format.'
    REQUEST_TIMEOUT = 'Request timed out. Please try again later.'
    INVALID_REQUEST = 'Invalid request.'
    INTERNAL_SERVER_ERROR = 'An internal server error occurred.'

    # authentication

    REGISTER_SUCCESED = 'Successfully registered.'
    REGISTER_FAILED = 'Registration failed. Please try again.'
    INVALID_CREDENTIALS = 'Invalid username or password.'
    EMAIL_ALREADY_IN_USE = ''
    PASSWORD_DOES_NOT_FOLLOW_SECURITY_REQUIREMENTS = ''
    AUTHENTICATION_FAILED = 'Authentication failed. Please try again.'

    # authorization

    PERMISSION_DENIED = 'Permission denied!'
    ROLE_NOT_FOUND = 'Role not found.'
    ROLE_IS_FULL = 'The role is full and cannot accept more users.'
    NOT_AUTHORIZED = 'You are not authorized to perform this action.'
