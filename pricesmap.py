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

from flask import \
        Flask,\
        render_template,\
        g
app = Flask(__name__)

from db_utilities import *


# == HOOKS ==
@app.before_request
def before_request():
    """ Pre-request hook """
    g.db = connect_db()

@app.teardown_request
def teardown_request(*args, **kw):
    """ Post request hook """
    g.db.close()


# == ROUTES & VIEWS ==
@app.route('/')
def home():
    """ Homepage view """

    return render_template('home.html')


if __name__=='__main__':
    app.run()
