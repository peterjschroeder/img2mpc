#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='img2mpc', 
        version='0.1', 
        description='Converts card images to mpc format.', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/img2mpc',
        scripts=['img2mpc'],
        install_requires=['pillow']
)

