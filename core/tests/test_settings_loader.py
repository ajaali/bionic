import unittest
import os
from core import Settings


class TestSettings(unittest.TestCase):
    def test_singleton_creation(self):
        """
        Test to make sure that the settings class is a singleton
        """
        yaml_doc = """
        name: DocuStore
        """

        s1 = Settings(yaml_stream=yaml_doc)
        s2 = Settings()
        self.assertEqual(id(s1), id(s2))

    def test_file_loading(self):
        """
        Check that the file path passed in the loaded correctly
        """
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "mock_settings1.yaml")
        s = Settings(file_path=file_path)
        self.assertDictEqual(s, {'name': 'Testing'})


    def test_error_when_no_yaml_provided(self):
        """
        Check that a Runtime Error is raised when an input is not provided
        """
        with self.assertRaises(RuntimeError):
            Settings()

    def test_error_when_yaml_cannot_be_parsed(self):
        """
        Check that an error is raised if the settings module is malformated
        """
        yaml_doc = """
        ijfisdjfi --- jidsjfidsjfi
        """
        with self.assertRaises(RuntimeError):
            Settings(yaml_stream=yaml_doc)

    def test_empty_settings_raises_error(self):
        """
        Check an error is raised when the settings module is empty
        """
        yaml_doc = ""
        with self.assertRaises(RuntimeError):
            Settings(yaml_stream=yaml_doc)

    def test_file_loading_from_environ(self):
        """
        Check that the file path is read from the environment parameter when it is not prvided
        to the constructor
        """
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, "mock_settings2.yaml")
        os.environ['BIONIC_SETTINGS_FILE'] = file_path
        s = Settings()
        self.assertDictEqual(s, {'name': 'Testing2'})

if __name__ == '__main__':
    unittest.main()