#!/usr/bin/python
import sys
import csv
infile = sys.stdin
#next(infile)

for line in infile:
    line = line.strip()
    my_list = line.split(',')

    # avoid lines starting with version and info to process
    if(my_list[0]=='ball'):
        # val= [no_of_deliveries, no_of_runs, no_of_wickets]
        val=[1] # no_of_deliveries for 1 record
        key=(my_list[6],my_list[4]) # batsman in column 4 and bowler in column 6
        val.append(int(my_list[7])+int(my_list[8])) # no_of_runs in record with extras
        #ensuring that runouts and no wickets are not counted

        print('%s:%s' % (str(key),str(val)))
    

			   
