from setuptools import setup

setup(
    name='dj-settings-helpers',
    version='1.0.0',
    url='https://github.com/tswicegood/dj-settings-helpers',
    license='Apache',
    author='Travis Swicegood',
    author_email='travis@domain51.com',
    description='Simple helpers for setting up your Django settings file',
    long_description=open('README.rst').read(),
    py_modules=['dj_settings_helpers'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
