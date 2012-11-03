dj-settings-helpers
===================
Simple helpers for setting up your Django settings file

.. image:: https://secure.travis-ci.org/tswicegood/dj-settings-helpers.png?branch=master

Usage
-----
Inside your ``settings.py`` file, do the following::

    from dj_settings_helpers import create_project_dir, get_env
    project_dir = create_project_dir(__file__)

Now, you can use ``project_dir`` to generate paths relative to your
``settings.py`` file and ``get_env`` to load environment variables.

For example, you can use it to add your ``project_root/templates``
directory to your ``TEMPLATES_DIRS`` setting like this::

    TEMPLATES_DIRS = (
        project_dir('templates'),
    )

You can use the ``get_env`` variable to pull in environment variables with
defaults that depend on the ``ENVIRONMENT`` variable.  For example, you can set
multiple default ``BROKER_HOST`` variables for Celery like this::

    BROKER_HOST = get_env('BROKER_HOST', 'default.rabbitmq.example.com',
            dev='localhost', staging='staging.rabbitmq.example.com')

If your ``ENVIRONMENT`` variable is equal to ``dev``, the ``localhost`` string
is used; if set to ``staging``, it is ``staging.rabbitmq.example.com``, and all
other environments use ``default.rabbitmq.example.com``.  All of these are
overridden by the presence of an environment variable named ``BROKER_HOST``.

Please see the inline documentation in ``dj_settings_helpers.py`` for full
examples and usage.


Installation
------------

::

    pip install dj-settings-helpers


License
-------
Copyright 2012 Travis Swicegood

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
