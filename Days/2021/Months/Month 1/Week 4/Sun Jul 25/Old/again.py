#! python 3.9.2
# Start
# Rewriting the programm 
# Modules
import hashlib
from exceptions import InvalidPassword, InvalidUsername, NotLoggedInError, NotPermittedError
from exceptions import UsernameAlreadyExists, PasswordToShort
from exceptions import PermissionError

class User:
    """User class who takes a usename and a password and shell
    save the password encrypted"""

    def __init__(self, username:str, password:str):
        """Creates a new user object.the password will be
        encrypted before storing"""

        self.username = username
        self.password = self._encrypt_pw(password)
    
    def _encrypt_pw(self, password):
        """Encrypt the password with the username and 
        return the sha digit"""

        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for
        the entered user, false otherwise."""

        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    """Map the user to the asked user account"""

    def __init__(self):
        """Construct an authenticator to manage
        users logging in and out."""

        self.users = {}
        
    def add_user(self, username:str, password:str):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        
        if len(password) < 8 or not password.isalnum():
            raise PasswordToShort(username)
        self.users[username] = User(username, password)
    
    def login(self, username:str, password:str):
        try:
            user = self.users[username]
        
        except KeyError:
            raise InvalidUsername(username)
        
        if not user.check_password(password):
            raise InvalidPassword   
        
        user.is_logged_in = True
        return True
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        
        return False

authenticator = Authenticator()

class Authorizor:
    """Choos if the user have the permission to enter
    to the account"""
    
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}
    
    def add_permission(self, perm_name):
        """Create new permissions that user can be
        added to"""

        try:
            perm_set = self.permissions[perm_name]
        
        except KeyError:
            self.permissions[perm_name] = set()
        
        else:
            raise PermissionError("Permission Exists")
    
    def permit_user(self, perm_name, username):
        """Granet the given permission to the user"""

        try:
            perm_set = self.permissions[perm_name]

        except KeyError:
            raise PermissionError("Permission does not exist")
        
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            
            perm_set.add(username)

    def check_permission(self, perm_name:str, username:str):
        if not self.authenticator.is_not_logged_in(username):
            raise NotLoggedInError(username)

        try:
            perm_set = self.permissions[perm_name]

        except KeyError:
            raise PermissionError(username)
        
        else:
            if username not in perm_set:
                raise NotPermittedError("Permission does not exist")
            
            else:
                return True

authorizor = Authorizor(Authenticator)

authenticator.add_user("Sam", "Pashmaksdontdie2314")
authorizor.add_permission("Painter")
authorizor.check_permission("Painter", "Sam")

# End