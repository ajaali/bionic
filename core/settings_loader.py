"""
Purpose:
*. Read the settings file and create a singleton object holding the settings parameters
"""
import os

import yaml

class Singleton(type):
    """
    Singleton meta class
    """
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class Settings(dict):
    """
    Parses the settings file and holds the parameters
    """
    __metaclass__ = Singleton

    def __init__(self, yaml_stream=None, file_path=None):
        """
        yaml_stream -- takes a stream object and loads it using PyYaml safe_load
        file_path -- alternative to passing in a stream, this will open the file and load it using
                     PyYaml safe_load
        """
        parsed_yaml = None
        if yaml_stream:
            parsed_yaml = yaml.safe_load(yaml_stream)
        elif not file_path and os.environ.get('DOCUSTORE_SETTINGS_FILE'):
            file_path = os.environ['DOCUSTORE_SETTINGS_FILE']
        elif file_path:
            with open(file_path, 'r') as yaml_file:
                parsed_yaml = yaml.safe_load(yaml_file)
        else:
            raise RuntimeError("Cannot locate settings module.  Have you set the 'DOCUSTORE_SETTINGS_FILE' enviornment variable")
        if parsed_yaml is None:
            raise RuntimeError("Error while parsing settings file")
        try:
            self.update(parsed_yaml)
        except ValueError, e:
            raise RuntimeError("Settings module malformated\n%s\n%s" % (e, parsed_yaml))