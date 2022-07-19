#! python 3.9.2
# Start
# Save all the exceptions of the user inserting

class AuthException(Exception):
    """The base class of the Authentication Error
    shell occure everry time the user tryes to enter
    something wrong about the username or password"""

    def __init__(self, username:str, user:str=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass

class PasswordToShort(AuthException):
    super().__init__("""Length of the password is to short or
    password you entered does not have any words""")

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class PermissionError(Exception):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

# End