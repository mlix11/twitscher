#!/usr/bin/env python3
import os
import glob
from setuptools import setup
from setuptools import find_packages


version = "0.1.0"
package_name = "twitscher"

setup(
    name=package_name,
    version=version,
    packages=find_packages(package_name),
)
