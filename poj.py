#! /usr/bin/python

import yaml

from lib import *
import os

'''First part '''
def load_config():
    config_d = 'config.yml'
    pydic    = yaml.load(file(config_d, 'r'))
    account  = Account(pydic['username'], pydic['password'])
    return account

if __name__ == '__main__':
    usage = 'Usage : just run it, maybe add option for just approved, error or others'
    
    account = load_config()
    robot   = Downloader(account)
    parser  = Parser(robot)
    save    = Save(robot)

    print 'Downloading problem sets to raw HTML ... '
    html = robot.download_problem_sets()
    print 'Done'

    print 'Parsing problem from raw HTML ... '
    probs = parser.parse_sets(html)
    print 'Done'

    print 'Generating problem diectory for probs ...'
    save.create_dirs(account.username)
    print 'Done'

    for id in probs:
        print 'Generate for problem', id
        html = robot.download_problem(probs[id])
        status, doc = parser.parse_sol(id, probs[id], html)

        if status == False: 
            print 'Failed in Parse this problem'
            continue
            
        status = save.save_problem(id, probs[id], doc)
        
        if status == False: print 'Failed in Save this problem'