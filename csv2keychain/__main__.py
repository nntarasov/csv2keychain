# -*- coding: utf-8 -*-

"""csv2keychain.__main__: contains entry point main()"""

import sys
from .csv2keychain import Csv2Keychain

__version__ = "0.1.0"


def main():
    print()
    print("Executing csv2keychain version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print()
    Csv2Keychain()
