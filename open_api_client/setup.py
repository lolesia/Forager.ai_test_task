"""Configuration file for creating a package."""
from setuptools import find_packages, setup

setup(
    name='nasa_open_api_client_test_task',
    version='0.1',
    packages=find_packages(),
    description='A Python client for accessing NASA Open API endpoints.',
    long_description="""
    This package provides a simple Python client for retrieving information from NASA Open API.
    It currently supports two endpoints: astronomy_picture_of_the_day and interplanetary_shock.
    """,
    author='Shevchenko Alessa',
    author_email='alesyavaskovith@gmail.com',
    install_requires=[
        'requests',
    ],
)
