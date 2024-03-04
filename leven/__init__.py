from os import path as _path
from ._levenshtein import levenshtein

__version__ = '1.0.4'


def get_include():
    return _path.abspath(_path.dirname(__file__))
