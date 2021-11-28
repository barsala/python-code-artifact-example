import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='barsala-test-package',
    long_description=README,
    version='1.0.0',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=['barsala_example', 'tests'],
    url='https://github.com/barsala',
    license='MIT',
    author='Michael Copley',
    author_email='engineering@barsala.com',
    description='This is a test python package will be stored in AWS CodeArtifact'
)
