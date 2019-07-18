"""Setup script for zmq_pub_sub"""

from setuptools import setup

requirements = [
    'zmq'
]

setup(name='zmq_pub_sub',
        version='0.1.0',
        author='Jacky Liang',
        author_email='',
        package_dir = {'': '.'},
        packages=['zmq_pub_sub'],
        install_requires=requirements
        )