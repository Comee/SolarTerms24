# -*- coding:utf-8 -*-
from SolarTerms import paiYue
from Util import init, PROJECT_ROOT

if __name__ == '__main__':
    years = init("input.ini")
    fpath = "%s\\output\\output.txt" % PROJECT_ROOT
    f = open( fpath , "w")
    for i in range(len(years)):
        print >> f, paiYue(years[i]),'\n'
    f.close()
    print '==============finished!============'
