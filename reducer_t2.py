#!/usr/bin/python
import csv
from operator import itemgetter
import sys

# resultant dictionary
res=dict()
for line in sys.stdin:
    line = line.strip()
    line_val = line.split(":")
    key, val = line_val[0], line_val[1]
    # print(type(key),type(val))
    try:
        # formatting key
        key=key.split("(")
        key=key[1]
        key=key.split(")")
        key=key[0]
        key=key.split(",")
        key[1]=key[1][1::] # removes the first element " " (space)

        # formatting val
        val=val.split("[")
        val=val[1]
        val=val.split("]")
        val=val[0]
        val=val.split(",")

        
        ball_count = int(val[0]) 
        run_count = int(val[1])
        wicket_count = int(val[2]) 

    except ValueError:
        print("ValueError")
        continue

    # removing single quotes from names of batsman and bowler
    key[0]=key[0][1:len(key[0])-1]
    key[1]=key[1][1:len(key[1])-1]

    key=tuple(key)
    
    if(key in res.keys()):
        res[key][0]+=ball_count
        res[key][1]+=run_count
        res[key][2]+=wicket_count
    else:
        res.update({key:[ball_count,run_count,wicket_count]})


for key in res.keys():
    if(res[key][0]>5):
        print('%s,%s,%s,%s' % (str(key[0]),str(key[1]), str(res[key][2]),str(res[key][0])))
