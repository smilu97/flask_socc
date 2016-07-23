#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Python SOCC server program
"""

#### Outers

from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
from contextlib import closing

#### Customs

import ChatRoom

DATABASE = '/tmp/soccFlask.db'
DEBUG = True
SECRET_KEY = 's00cc'
USERNAME = 'socc'
PASSWORD = 's00cc1234'

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request() :
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception) :
    g.db.close()

def init_db() :
    with closing(connect_db()) as db :
        with app.open_resource('schema.sql') as f :
            db.cursor().executescript(f.read())
        db.commit()

def connect_db() :
    return sqlite3.connect(app.config['DATABASE'])

############## http

@app.route('/', methods=['GET'])
def firstPage() :
    return render_template('index.html')

############# ajax

@app.route('/api/get/userlist', methods=['GET'])
def ApiGetUserlist() :
    pass

@app.route('/api/post/create_user', methods=['POST'])
def ApiPostCreateUser() :
    pass

###################### About Chat Room

@app.route('/api/post/post_message', methods=['POST'])
def ApiPostPostMessage() :
    pass

@app.route('/api/get/EnterChatRoom', methods=['GET'])
def ApiGetEnterChatRoom() :
    pass

@app.route('/api/get/EscapeChatRoom', methods=['GET'])
def ApiGetEscapeChatRoom() :
    pass



def __name__ == '__main__' :
    app.run(host='0.0.0.0')
