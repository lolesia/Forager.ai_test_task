from setuptools import setup

setup(
    name='Nasa_open_api',
    version='0.1.0',
    description='Receive and manage data from two endpoints Nasa Open APi',
    install_requires=open('requirements.txt').read().strip().split('\n'),
)