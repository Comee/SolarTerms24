# -*- coding:utf-8 -*-
'''
Created on 2014年2月13日

@author: xuer
'''

#coding=gbk
import logging
import os


if __name__ == '__main__':
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),level = logging.WARN, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')
    print os.getcwd()
    print os.path.join(os.getcwd(), 'input','log.txt')
    print os.path.join(os.getcwd(), 'log.txt')
    logging.debug('debug')    #被忽略
    logging.info('info')    #被忽略
    logging.warning('warn')
    logging.error('error')
