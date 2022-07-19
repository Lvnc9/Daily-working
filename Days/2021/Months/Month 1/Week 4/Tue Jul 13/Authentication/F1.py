#! python3
# Start
# Act as the first part of the whole program. wil do the authentication part of the program
# Modules
import hashlib

class User:
    """Store the users account
    Encrypte it and make it a litle bit more secure
    !! password will be encrypted before storing"""
    
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = self._encrypte_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest"""
        hash_string = (self.username + password)
        hash_string = hash_string.encode('utf8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid fot this
        user, False otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password
    
### Authotication excpetion classes 
# for making the accounts more secure ###

class AuthException(Exception):
    def __init__(self, username, user=None):
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordToShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class Authenticator:
    def __init__(self):
        """Construct an authenticator to manage user logging
        in, and out."""

        self.users = dict()

    def add_user(self, username:str, password:str):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) > 8:
            raise PasswordToShort(username)
        self.users[username] = User(username, password)

    def login(self, username:str, password:str):
        try:
            user = self.users[username]
        
        except KeyError:
            raise InvalidUsername
        
        if not User.check_password(password):
            raise InvalidPassword(username, password)

        user.is_logged_in = True
        return True
    
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

authenticator = Authenticator()

class Authorizer:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name:str):
        """Create new premisions that new users can be
        added to"""

        try:
            perm_set = self.premissions[perm_name]
        except KeyError:
            self.permisions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")
        
    
    def permit_user(self, perm_name:str, username:str):
        """Grant the given permission to the user"""

        try:
            perm_set = self.permissions[perm_name]

        except KeyError:
            raise PermissionError("Permission Does not exist")
        
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

# End