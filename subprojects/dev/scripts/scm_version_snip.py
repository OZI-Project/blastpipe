"""python snippet: grab version info"""
from setuptools_scm import get_version
print(get_version(normalize=False))
