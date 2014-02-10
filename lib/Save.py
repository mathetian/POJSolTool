#! /usr/bin/python

import os

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
    	file = open(filename, 'w')
    	try:
    		file.write(doc)
    	except:
    		print 'maybe encode problem, notice %s %s'%(id, runid)
    	file.close()