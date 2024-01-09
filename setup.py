from setuptools import setup, find_packages

setup(
    name='nasa_open_api',
    version='0.1',
    packages=find_packages(include=['core', 'nasa_api']),
    description='Receive and manage data from two endpoints Nasa Open APi',
    install_requires=open('requirements.txt').read().strip().split('\n'),
)
