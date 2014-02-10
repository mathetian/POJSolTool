#! /usr/bin/python
# coding=utf-8

import urllib
import urllib2
import cookielib

class Downloader:
    def __init__(self, account):
        self.ROOT    = 'http://poj.org'
        self.LIMIT   = 10

        self.account = account
        self.status = self.login()
    
        if self.status == 0: print 'Login Failed'
        else: print 'Login Successfully'
    
    def login(self):
        #build it, global, like class in C++
        processor = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        opener  = urllib2.build_opener(processor)
        urllib2.install_opener(opener)

        params = urllib.urlencode({'user_id1': self.account.username, 
                                   'password1': self.account.password, 
                                   'B1': 'login','url' : '.'})

        #urlopen is also can be written as opener.open(uri, params, header)
        #can get header, url, read() from response
        uri = self.ROOT + '/login'
        content = urllib2.urlopen(uri, params).read()

        #check it to judge whether it is correct
        if content.find('Log Out') != -1: return True
        else: return False

    def download_problem_sets(self):
        params = urllib.urlencode({'user_id': self.account.username})

        uri = self.ROOT + '/userstatus?' + params

        html = self.download(uri)
        return html

    def download_problem_runid(self, pm):
        params = urllib.urlencode({'problem_id': pm, 
                                   'user_id': self.account.username, 
                                   'result': '0','language' : ''})

        uri = self.ROOT + '/status?' + params
        #use this link to get Run ID, just get the first id
        html = self.download(uri)
        return html

    def download_problem(self, runid):
        params = urllib.urlencode({'solution_id': runid})
        uri = self.ROOT + '/showsource?' + params
        #use this link to get sol
        html = self.download(uri)
        return html

    def download(self, uri):
        content = urllib2.urlopen(uri)
        return content.read()

if __name__ == '__main__':
    pass