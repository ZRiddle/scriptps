#!/usr/bin/env python

import setuptools

PROD_DEPENDENCIES = [
    "appscript==1.2.0",
    "click<=8.0.4",
    "pyobjc==8.5",
]

setuptools.setup(
    name='scriptps',
    version='1.0.1',
    url="https://github.com/ZRiddle/scriptps",
    description='Photoshop scripting with python using macOS',
    author='Zach Riddle',
    author_email='zdriddle@gmail.com',
    install_requires=PROD_DEPENDENCIES,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "psa=cli.psa:psa",
        ]
    }
)
