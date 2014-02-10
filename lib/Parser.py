#! /usr/bin/python
# coding=utf-8

from BeautifulSoup import BeautifulSoup

import re
import sys
from time import sleep

class Parser:
    def __init__(self, robot):
        self.robot = robot
    
    def parse_sets(self, html):
        #use regex to parse the set id
        pattern = re.compile('p\([0-9]{4}\)',re.DOTALL)
        ids     = re.findall(pattern, html)

        result  = {}
        for id in ids:
            id = id[2:-1]  
            html = self.robot.download_problem_runid(id)
            rs = self.parse_runid(id, html)
            if rs is not None: result[id] = rs

            print '%s has been pre-processed' % (id)

        return result

    def parse_runid(self, id, html):
        try:
            soup  = BeautifulSoup(html)
            body  = soup.body
            table = body.table.nextSibling.nextSibling.nextSibling
            tr    = table.tr
            td    = tr.findNext('tr').td
            return str(td.contents[0])
        except:
            print 'we will sleep 5000ms, please wait'
            sleep(5)
            try:
                soup  = BeautifulSoup(html)
                body  = soup.body
                table = body.table.nextSibling.nextSibling.nextSibling
                tr    = table.tr
                td    = tr.findNext('tr').td
                return str(td.contents[0])
            except:
                print 'sorry something error with problem: ', id
                return None

    def parse_sol(self, id, runid, html):
        try:
            soup  = BeautifulSoup(html)
            ul    = soup.body.ul
            pre   = ul.pre
            doc   = self.traverse(pre.contents[0])
            return True, doc
        except:
            print 'we will sleep 5000ms, please wait'
            sleep(5)
            try:
                #ugly
                html  = robot.download_problem(runid)
                soup  = BeautifulSoup(html)
                ul    = soup.body.ul
                pre   = ul.pre
                doc = self.traverse(pre.contents[0])
                return True, doc
            except:
                print 'sorry something error with problem: ', id
                return False, ""
        pass

    def traverse(self, doc):
        doc = doc.replace('&lt;', '<')
        doc = doc.replace('&gt;', '>')
        doc = doc.replace('&#34;', '\"')
        doc = doc.replace('&#39;', '\'')
        doc = doc.replace('&#38;', '&')
        return doc