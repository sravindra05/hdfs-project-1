#!/usr/bin/python
import sys
import csv
infile = sys.stdin
#next(infile)

#fuel column index 8
for line in infile:
    line = line.strip()
    my_list = line.split(',')
    if(my_list[0]=='ball'):
        val=[1]
        key=(my_list[4],my_list[6])
        val.append(my_list[7])
        if(my_list[9]!="" and my_list[9]!="run out"):
            val.append(0)
        else:
            val.append(1)
        print('%s:%s' % (str(key),str(val)))
    

			   
