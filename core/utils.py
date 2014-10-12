"""
Purpose:
*. Utility functions
    - Logging
"""

import logging
from settings_loader import Settings

def initLogger():
    """
    Initialise the logging object from the settings module
    """
    settings = Settings()
    if "logging" in settings:
        logging.config.dictConfig(settings['logging'])
