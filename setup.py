from setuptools import setup

from colors import __author__
from colors import __email__
from colors import __program__
from colors import __url__
from colors import __version__


setup(
    author=__author__,
    author_email=__email__,
    install_requires=[],
    name=__program__,
    packages=[__program__],
    platforms='all',
    setup_requires=[
        'setuptools',
        'tox',
    ],
    test_suite='tests',
    url=__url__,
    version=__version__,
)
