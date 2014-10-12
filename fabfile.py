import os

from fabric.api import *

env.hosts = ['ahmed@192.168.1.86']
env.password = 'qwerty'

def project_dir():
    """
    Get the bionic project dir
    """
    if 'bionic' in os.environ:
        return os.environ['bionic']
    else:
        return os.path.dirname(os.path.realpath(__file__))
    return current_file_path


def deploy_schema():
    """
    Deploy the local copy of the database schema onto the remote database
    """
    schema_dir = os.path.join(project_dir(), "db")
    remote_dir = '/tmp/db'
    put(schema_dir, '/tmp')
    with settings(sudo_user="postgres"):
        with cd(remote_dir):
            sudo("psql -d template1 -f clean_setup.sql")
            sudo("psql -d template1 -f app_setup_schema.sql")
            sudo("psql -d template1 -f app_store_schema.sql")





