import unittest
from mock import patch
from core import Application


class TestApplication(unittest.TestCase):
    """
    Tests for the application class
    """
    def test_new_application(self):
        """
        Test the creation of a new application
        """
        app = Application("NewApp")
        self.assertFalse(app.installed)
        self.assertEqual(app.app_name,"NewApp")
        self.assertNotEqual(app.app_key, "")

    def test_load_application_by_app_name(self):
        """
        Test the loading of applications when the name is provided
        """
        with patch('core.application.get_app_key') as mock_f:
            mock_f.return_value = "Mock App Key"
            app = Application.get(app_name="SomeApp")
            self.assertEqual(app.app_name,"SomeApp")
            self.assertEqual(app.app_key, "Mock App Key")
            self.assertTrue(app.installed)

    def test_load_application_invalid_app_name(self):
        """
        Test the loading of applications when an invalid name is provided
        """
        with self.assertRaises(ValueError):
            with patch('core.application.get_app_key') as mock_f:
                mock_f.side_effect = ValueError
                Application.get(app_name="Invalid")

    def test_load_application_by_app_key(self):
        """
        Test the loading of an application using its app_key
        """
        with patch('core.application.get_app_name_from_key') as mock_f:
            mock_f.return_value = "SomeApp"
            app = Application.get(app_key="SomeKey")
            self.assertEqual(app.app_name,"SomeApp")
            self.assertEqual(app.app_key, "SomeKey")
            self.assertTrue(app.installed)

    def test_load_application_invalid_app_key(self):
        """
        Test the loading of an application using an invalid app_key
        """
        with self.assertRaises(ValueError):
            with patch('core.application.get_app_name_from_key') as mock_f:
                mock_f.side_effect = ValueError
                Application.get(app_key="SomeKey")



if __name__ == '__main__':
    unittest.main()
