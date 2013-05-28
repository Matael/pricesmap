#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# pricesmap.py
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
PricesMap
=========

Price tracking for some products in the city.
PricesMap allow everyone to add a price and a pic for some product for example expressos...
"""

import sqlite3

from flask import \
        Flask,\
        render_template
app = Flask(__name__)


@app.route('/')
def home():
    """ Homepage view """

    return render_template('home.html')




if __name__=='__main__':
    app.run()
