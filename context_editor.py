#!/usr/bin/python
# coding: utf-8

#################################################################################################

import xbmc
import sys

from resources.lib.dialog_metadata import *

#################################################################################################

if __name__ == "__main__":
    listitem = sys.listitem.getVideoInfoTag()
    dbid = listitem.getDbId()
    dbtype = listitem.getMediaType()
    EditDialog({'dbid': dbid, 'type': dbtype})