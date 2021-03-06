import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-decadence',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License', 
    description='Dynamic frontend library for people who hate JS frameworks',
    long_description=README,
    url='https://www.krojony.pl/',
    author='Maciej Janiszewski',
    author_email='chleb@krojony.pl',
    install_requires=[
        "django<2",
        "channels~=1.1.8"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10', 
        'Framework :: Django :: 1.11', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)