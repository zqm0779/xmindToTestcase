# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/4 19:59
@Auth ： zhangqimin
@File ：setup.py
@IDE ：PyCharm

"""
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='UiA',
    keywords='',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='snailgirl',
    #author_email='test@sina.com',
    description='',
    install_requires=[
        'xmindparser',
        "xlwt"
    ]
)