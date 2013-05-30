#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# db_utilities.py
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
Some utilities for Database
"""

import sqlite3

from settings import *

# database
def connect_db():
    """ Connection to database """
    return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False, conn=None):
    """ DB Helper Function
    If conn is provided, works on this connection, else, work on default connection
    """

    if conn:
        cur = conn.execute(query, args)
    else:
        cur = g.db.execute(query, args)

    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv



