# -*- coding:utf-8 -*-
'''
Created on 2014年2月16日

@author: xuer
'''
import os
from ConfigParser import ConfigParser 
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def init(filename):
    global  PROJECT_ROOT
    CONFIGFILE = filename
    configPath = PROJECT_ROOT + '\\input\\' + CONFIGFILE
    config = ConfigParser()    
    config.read(configPath)
    alist = str(config.get('ConfigOrParameters', 'cop')).replace(' ', '').split(',')
    return alist
