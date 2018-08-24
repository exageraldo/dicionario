from setuptools import setup, find_packages
import os

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, 'requirements.txt')) as _file:
    requirements = [line.strip() for line in _file]

setup(
    name='pydicts',
    version='v0.1.1',
    packages=find_packages(),
    install_requires=requirements,
    license='MIT',
    author='Victor Matheus de Castro Geraldo',
    author_email='victormatheuscastro@gmail.com',
    description='Unofficial Python API for Dicio and DicionarioInformal'
)