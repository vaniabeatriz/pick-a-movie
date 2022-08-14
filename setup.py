from setuptools import setup, find_packages

# The setup tools is a library that helps in building, distributing, and installing modules required to run the App.

setup(
    name='Decision Making App',
    version='1.0.0',
    url='https://github.com/Z-Guo/Decision-Making-App.git',
    author='HelenPhoenixVaniaZiling',
    description='A make a browser-style decision making application to choose a movie to watch',
    packages=find_packages(),
    install_requires=['flask >= 2.1', 'requests'],
)