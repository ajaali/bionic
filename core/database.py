"""
Purpose:
*. Provide the database interface to the functionality in the docustore application
"""

import psycopg2
import psycopg2.extensions
# Register typcasters to return all strings as UNICODE
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


def get_app_key(app_name):
    """
    For a given application app_name return the app_key
    """
    return ""

def get_app_name_from_key(app_key):
    """
    For a given app_key return the app_name
    If the key doesn't exist a Value error will be raised
    """