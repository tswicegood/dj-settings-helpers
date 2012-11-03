import os


def create_project_dir(project_path):
    """
    Generates a project_dir function for use in Django settings modules

    You can create a ``project_dir`` function for your settings module
    using this function.  Provide it with the path to your settings
    module and returns a function that can combine that with any set of
    path elements to create a cross-platform path.

    Example::

        >>> project_dir = create_project_dir("/foobar/settings.py")
        >>> project_dir("templates")
        '/foobar/templates'

    Generally, you would use this as ``create_project_dir(__file__)``.
    """
    def project_dir(*paths):
        base = os.path.realpath(os.path.dirname(project_path))
        return os.path.join(base, *paths)

    return project_dir


def get_env(key, default, force_bool=False, type_func=None, **defaults):
    """
    Returns the correct environment variable

    This provides a few useful additions on top of a generic call to
    ``os.environ.get(key, default)``.  First, you can coerce a value
    into a boolean by using the kwarg ``force_bool=True``.  For example:

    ::

        >>> import os
        >>> os.environ['some-value'] = 'Yes'
        >>> get_env('some-value', 'default', force_bool=True)
        True

    This works with ``yes``, ``true``, and ``1``.  Capitalization is
    ignored for all of these.

    Next, you can provide a ``type_func`` to force a conversion to a
    particular type.  This is useful for values that need to be an
    integer, since everything in ``os.environ`` is a string.  For
    example:

    ::

        >>> os.environ['some-int'] = '1234'
        >>> get_env('some-int', 'default', type_func=int)
        1234

    Finally, you can provide extra defaults that change depending on the
    environment.  For example, let's say you have a dev and testing
    environment you can use ``get_env`` like this:

    ::

        >>> os.environ['ENVIRONMENT'] = 'testing'
        >>> get_env('some-key', 'default', dev='dev', testing='testing')
        'testing'
        >>> os.environ['ENVIRONMENT'] = 'dev'
        >>> get_env('some-key', 'default', dev='dev', testing='testing')
        'dev'

    """
    env = os.environ.get('ENVIRONMENT')
    a = os.environ.get(key, defaults.get(env, default))
    if force_bool:
        return str(a).lower() in ['1', 'yes', 'true', ]
    return a if type_func is None else type_func(a)
