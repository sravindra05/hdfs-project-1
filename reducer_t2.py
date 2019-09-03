#!/usr/bin/python
import csv
from operator import itemgetter
import sys

# current_count = 0
# current_key = ""
res=dict()
for line in sys.stdin:
    line = line.strip()
    line_val = line.split(":")
    key, val = line_val[0], line_val[1]
    try:
        val=val.split("[")
        val=val[1]
        val=val.split("]")
        val=val[0]
        val=val.split(",")
        ball_count = int(val[0]) 
        run_count = int(val[1])
        wicket_count = int(val[2]) 
    except ValueError:
        continue
    # global current_key
    # global current_count
    if(key in res.keys()):
        res[key][0]+=ball_count
        res[key][1]+=run_count
        res[key][2]+=wicket_count
    else:
        res.update({key:[ball_count,run_count,wicket_count]})
    
for key in res.keys():
    if(res[key][0]>5):
        print('%s,%s,%s,%s' % (key[0],key[1], res[key][2],res[key][0]))
