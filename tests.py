import os
import types
import unittest

from dj_settings_helpers import create_project_dir


class TestOfProjectDirGenerator(unittest.TestCase):
    def generate_expected_path(self, base, *paths):
        return os.path.join('/', base, *paths)

    def test_returns_a_function(self):
        f = create_project_dir('foo')
        self.assertTrue(type(f) is types.FunctionType)

    def test_returned_function_returns_path(self):
        project_dir = create_project_dir('/foo/settings.py')
        expected = self.generate_expected_path('foo', 'templates')
        self.assertEqual(expected, project_dir('templates'))

    def test_can_combine_multiple_paths(self):
        project_dir = create_project_dir('/foo/settings.py')
        expected = self.generate_expected_path('foo', 'templates', 'config')
        self.assertEqual(expected, project_dir('templates', 'config'))
