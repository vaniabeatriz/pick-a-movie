from setuptools import setup, find_packages

setup(
    name='Decision Making App',
    version='1.0.0',
    url='https://github.com/Z-Guo/Decision-Making-App.git',
    author='HelenPhoenixVaniaZiling',
    description='A make a browser-style decision making application to choose a movie to watch',
    packages=find_packages(),
    install_requires=['flask >= 2.1', 'requests'],
)