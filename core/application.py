"""
Purpose:
*. Manage application setup in Docustore
"""

import uuid



class Application(object):
    """
    DocuStore manages documents on behalf of applications.  This class allows you to:
    *. Create a new application and install it
    *. Retrieve applications already installed
    *. Inspect application settings and permissions and ammend them
    *. Disable applications
    *. Uninstall applications
    """
    def __init__(self, app_name):
        """
        Create a new application with the app_name
        """
        self._installed = False
        self._app_name = app_name
        self._app_key = str(uuid.uuid4())
        self._settings = {}

    @staticmethod
    def get(app_name=None, app_key=None):
        """
        Retrieve an application from the store
        app_name -- Application Name
        app_key -- Application UUID
        """

    @property
    def installed(self):
        """
        True if the application is installed
        """
        return self._installed

    @property
    def app_key(self):
        """
        The application app_key
        """
        return self._app_key

    @property
    def app_name(self):
        """
        The application app_name
        """
        return self._app_name

    def install(self):
        """
        Install the a new application
        """


class User(object):
    """
    Represents the application user
    *. Create a new User
    *. Set a password
    *. Manage user details
    """
    def __init__(self, username=None, password=None, email=None):
        self._user_id = None
        self._username = username
        self._password = password
        self._email = email
        self._details = {}

    def save(self):
        """
        Save the user object to the database
        """

    @property
    def username(self):
        """
        The username
        """
        return self._username

    @property
    def password(self):
        """
        The password
        """
        return self._password

    @property
    def email(self):
        """
        The email address
        """
        return self._email

    @staticmethod
    def get(username=None, email=None):
        """
        Retrieve a user
        """

class Group(object):
    """
    Manages the application groups.  Groups join Application, Users and Permissions
    """
    def __init__(self):
        self._group_id = None
        self._app_key = None
        self._group_name = None

    @property
    def application(self):
        """
        Retrieve the application attached to this groups
        """
        return Application.get(app_key=self._app_key)

    @property
    def users(self):
        """
        Return the users attached to this application
        """
        return []

    @property
    def permissions(self):
        """
        Return the list of permissions attached to the group
        """
        return []

    def add_user(self, user):
        """
        Add a user to the group
        """

    def add_permission(self, permission):
        """
        Add a permission to the group
        """
