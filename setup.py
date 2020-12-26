import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='registration',
    version='0.2',
    packages=['registration'],
    include_package_data=True,
    license='GPLv2',
    description='A simple Django app to manage users login/logout and registration.',
    long_description=README,
    url='https://github.com/hcosta/django-easyregistration',
    author='Hector Costa',
    author_email='hey@hektor.dev',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
       'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)