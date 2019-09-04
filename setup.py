import os
from setuptools import setup, find_packages


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT_DIR, 'README.md'), 'r') as readme:
    long_description = readme.read()

setup(
    name='antiafk',
    version='1.0.0',
    description='Antiafk has been designed to utilize the pynput package by creating a cli that allows the user to specify a key to be to be triggered on interval.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='cli wow world of warcraft classic afk keypress automated',
    url='https://gitlab.com/rburns629/antiafk',
    author='Robert Burns',
    author_email='rburns629@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    project_urls={
        'Bug Reports': 'https://gitlab.com/rburns629/antiafk/issues',
        'Source': 'https://gitlab.com/rburns629/antiafk',
    },
    install_requires=[
        'pynput',
        'pytest', 
        'click',
        'markdown'
    ],
    entry_points={
        'console_scripts': ['antiafk=antiafk:cli']
    }
)


    