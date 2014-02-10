#! /usr/bin/python
# coding=utf-8

import os
import codecs
import sys

#notice it
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

class Save:
    def __init__(self, robot):
        self.robot = robot

    def create_dirs(self, dir):
        if not os.path.exists(dir):
        	os.makedirs(dir)
        os.chdir(dir)

    def save_problem(self,id, runid, doc):
    	#to simplify our requirement, I assume `cpp`.
    	filename = '%s.cpp'%(id)
        
        #notice the solution, very important
        file = codecs.open(filename, 'w', encoding='utf-8')
        
        try:
    		file.write(doc)
    	except:
            print doc
            print 'maybe encode problem, notice %s %s'%(id, runid)
    	file.close()