import os
import random
import types
import unittest

from dj_settings_helpers import create_project_dir, get_env


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


class TestOfGenEnv(unittest.TestCase):
    def test_returns_default_if_no_env_var_set(self):
        default = 'foobar'
        self.assertEqual(default, get_env('unknown-and-unknowable', default))

    def test_returns_env_var_if_set(self):
        a = '%s' % random.randint(1000, 2000)
        os.environ['some-test-key-%s' % a] = a
        self.assertEqual(a, get_env('some-test-key-%s' % a, 'default'))
        del os.environ['some-test-key-%s' % a]

    def test_returns_different_default_based_on_environment(self):
        default = 'foobar'
        dev_default = 'barfoo'
        os.environ['ENVIRONMENT'] = 'dev'

        self.assertEqual(dev_default, get_env('not-set', default,
                dev=dev_default))

    def test_can_force_to_boolean(self):
        self.assertTrue(get_env('foo', True, force_bool=True) is True)
        self.assertTrue(get_env('foo', '1', force_bool=True) is True)
        self.assertTrue(get_env('foo', 'yes', force_bool=True) is True)
        self.assertTrue(get_env('foo', 'true', force_bool=True) is True)
        self.assertTrue(get_env('foo', 'True', force_bool=True) is True)
        self.assertTrue(get_env('foo', 'TRUE', force_bool=True) is True)

        self.assertTrue(get_env('foo', False, force_bool=True) is False)
        self.assertTrue(get_env('foo', '0', force_bool=True) is False)
        self.assertTrue(get_env('foo', 'no', force_bool=True) is False)
        self.assertTrue(get_env('foo', 'false', force_bool=True) is False)
        self.assertTrue(get_env('foo', 'False', force_bool=True) is False)
        self.assertTrue(get_env('foo', 'FALSE', force_bool=True) is False)


    def test_can_be_coerced_by_a_func(self):
        def type_func(value):
            self.assertEqual(value, 'Hi, Dad!')
            return 'Hi, Mom!'

        result = get_env('foo', 'Hi, Dad!', type_func=type_func)
        self.assertEqual('Hi, Mom!', result)

    def test_coercion_function_receives_returned_value(self):
        value = 'foo-%s' % random.randint(1000, 2000)
        os.environ['random-value'] = value

        def type_func(a):
            self.assertEqual(a, value)

        get_env('random-value', 'default', type_func=type_func)
