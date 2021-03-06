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
        render_template, flash, make_response
from contextlib import closing
import hashlib
import json

#### Customs

import ChatRoom
import CRUDString

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



###################### http

@app.route('/', methods=['GET'])
def firstPage() :
    return render_template('index.html')

@app.route('/test/get/create/user', methods=['GET'])
def testCreateUser() :
    return render_template('test_createuser.html')

@app.route('/test/get/login', methods=['GET'])
def testLogin() :
    return render_template('test_login.html')

###################### Ajax

@app.route('/api/get/userlist', methods=['GET'])
def ApiGetUserlist() :
    cur = g.db.execute(CRUDString.ReadDB('users', ['no', 'name', 'id']))
    rows = cur.fetchall()
    return json.dumps(rows)

###################### Sign Up

@app.route('/api/post/create/user', methods=['POST'])
def ApiPostCreateUser() :
    user_name = request.form['name']
    user_id = request.form['id']
    user_password = request.form['password']
    cur = g.db.execute(CRUDString.CreateDB('users', ['name', 'id', 'password'], \
        [user_name, user_id, user_password]))
    g.db.commit()
    return redirect('/')

###################### Login

@app.route('/api/get/login/<string:id>/<string:password>', methods=['GET'])
def Login(id, password) :
    qs = CRUDString.ReadDB('users', ['no', 'name', 'id'], ['id', 'password'], \
        [id, password])
    cur = g.db.execute(qs)
    rows = cur.fetchall()
    if len(rows) == 1 :
        user = rows[0]
        session['user_no'] = user[0]
        session['user_name'] = user[1]
        session['user_id'] = user[2]
        return 'success'
    else :
        return 'fail'

###################### About Chat Room

@app.route('/api/post/create/chatroom', methods=['POST'])
def ApiPostCreateChatRoom() :
    if session.get('user_no', -1) == -1 :
        return 'login needed'


@app.route('/api/post/post_message', methods=['POST'])
def ApiPostPostMessage() :
    pass

@app.route('/api/get/EnterChatRoom', methods=['GET'])
def ApiGetEnterChatRoom() :
    pass

@app.route('/api/get/EscapeChatRoom', methods=['GET'])
def ApiGetEscapeChatRoom() :
    pass



if __name__ == '__main__' :
    app.run(host='0.0.0.0')
