#!/usr/bin/python

########################

from resources.lib.helper import *
from resources.lib.dialog import *

########################

class Main:
    def __init__(self):
        self.action = False
        self._parse_argv()
        EditDialog(self.params)

    def _parse_argv(self):
        args = sys.argv

        for arg in args:
            if arg == ADDON_ID:
                continue
            if arg.startswith('action='):
                self.action = arg[7:].lower()
            else:
                try:
                    self.params[arg.split("=")[0].lower()] = "=".join(arg.split("=")[1:]).strip()
                except:
                    self.params = {}

if __name__ == '__main__':
    Main()
