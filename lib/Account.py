#! /usr/bin/python
# coding=utf-8

'''Account'''
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def toStr(self):
        return self.username + "##" + self.password