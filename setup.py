"""Setup script for simple_zmq"""

from setuptools import setup

requirements = [
    'zmq'
]

setup(name='simple_zmq',
        version='0.1.1',
        author='Jacky Liang',
        author_email='',
        package_dir = {'': '.'},
        packages=['simple_zmq'],
        install_requires=requirements
        )