import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-gp-auth',
    version='1.0.0.dev1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='GP Auth is a simple application Django to manage the registration of users in a customized manner system',
    long_description=README,
    url='https://github.com/gilsonbp/gp-auth',
    author='Gilson Paulino',
    author_email='gilsonbp@gmail.com',
    keywords='Gilson Paulino GP Developer',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
