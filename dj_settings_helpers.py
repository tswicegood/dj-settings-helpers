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
