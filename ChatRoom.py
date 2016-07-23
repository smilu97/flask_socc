#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 becxer <becxer87@gmail.com>
#
# Distributed under terms of the MIT license.

"""
ChatRoom class
"""

class ChatRoomUser :
    def __init__(self) :
        self.no = -1 # -1 means not initialized
        self.name  = -1
    def isEqual(other) :
        if self.no == other.no :
            return True
        if self.name == other.name :
            return True
        return False
class ChatRoomMessage :
    def __init__(self) :
        self.user = 0
        self.msg = 0

class ChatRoom() :
    def __init__(self) :
        self.title = "default chat room title"
        self.in_users = []
        self.message = []
        self.usermap = {}
    def addUser(no, name) :
        tmpUser = ChatRoomUser() # Make new Object
        tmpUser.no = no
        tmpUser.name = name
        for users in in_users : # Overlap Check
            if not users.isEqual(tmpUser) :
                self.in_users.append(tmpUser) # Append Object
                self.usermap[no] = tmpUser # Set Usermap
    def addMessage(user_no, msg) :
        tmpMessage = ChatRoomMessage()
        tmpMessage.user = self.in_users[self.usermap[user_no]] # Find User
        tmpMessage.msg = msg
        self.message.append(tmpMessage)
        
