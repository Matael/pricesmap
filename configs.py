#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# configs.py
#
# Copyright © 2013 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""
Configuration reader/updater for PricesMap
"""

import os
import json
from sets import Set
from glob import glob

from db_utilities import *

def update_db():
    """
    Check the glob configs/*.json against table names
    """

    # get list of tables :
    conn = connect_db()
    tables = Set([_['name'] for _ in query_db("select name from sqlite_master where type='table' and name!='meta';", conn=conn)])

    # get list of files in configs/
    files  = Set([_.split('/')[1].split('.')[0] for _ in glob('configs/*.json')])

    # test for non unique elements
    for c in tables-files:
        print("{0} exists in DB but no config file was found".format(c))

    for c in files-tables:
        print("{0} found in files but not in DB, including it....")

        with open('configs/{}.json'.format(c)) as f:
            c_metas = json.loads(f.read())

        try:

            # create the table using specified structure
            print("--> Creating the table {}".format(c))
            result = query_db(c_metas['table_structure'], conn=conn, one=True)
            if result: print(result)



        except KeyError:
            print("At least one of the config files doesn't have the right format. Please fix that.")

    conn.close()
