from setuptools import setup
import sys

CLASSIFIERS = ['License :: OSI Approved :: MIT License']

setup(
    name="jstime",
    version = '1.0',
    maintainer='Luminoso, LLC',
    maintainer_email='dev@lumino.so',
    classifiers=CLASSIFIERS,
    url = 'http://github.com/LuminosoInsight/jstime',
    platforms = ["any"],
    description = "Convert python datatime objects to/from milliseconds from epoch",
    py_modules=['jstime'],
)
