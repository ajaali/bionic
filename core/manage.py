"""
Purpose:
*. Run application utilities from the command line.
"""
import os
import argparse
import logging
import logging.config
from settings_loader import Settings
from utils import initLogger
from db_conn import connectToDB

# Init logger to logging module
logger = logging

class Manage(object):
    """
    Sets the settings module path and runs the command
    """
    def __init__(self, settings_path=None):
        """
        settings -- full path to settings module
        """
        if settings_path is not None:
            Settings(file_path=settings_path)
        elif os.environ.get("BIONIC_SETTINGS_FILE") is None:
            module_path = os.path.dirname(__file__)
            settings_path  = os.path.join(module_path, "settings.yaml")
            os.environ["BIONIC_SETTINGS_FILE"] = settings_path
            Settings()
        else:
            Settings()
        initLogger()
        global logger
        logger = logging.getLogger("bionic")

    def run(self, command, args):
        """
        command -- Name of the command to run
        args -- Argument Parser
        """
        logger.debug("Going to run %s with %s", command, args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility to help manage DocuStore through the command line')
    parser.add_argument('--settings', action="store", help="Full path to the settings module.  By default points to BIONIC_SETTINGS_FILE env variable")
    subparsers = parser.add_subparsers(dest="command", help='command help')
    # Command: rebuild
    parser_rebuild = subparsers.add_parser('rebuild', help="Drop and Recreate the setup database")
    # Command: addapp
    parser_addapp = subparsers.add_parser('addapp', help="Install a new application")
    parser_addapp.set_defaults(command="addapp")
    parser_addapp.add_argument('--name', help="Name of the new application")
    # Parse and run
    args = parser.parse_args()
    manage = Manage(args.settings)
    manage.run(args.command, args)

