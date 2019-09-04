#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

cur_venue = ''  # venue of the match
cur_batsman=''  #batsman who batted
cur_ctr = 0 # total no of deliveries
cur_runs=0  #totl no of runs made
word = None

result={}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split(':')
    
    # convert count (currently a string) to int
        #reformatting the input given
    key_attr=key.split('\'')
    venue=key_attr[1]
    batsman=key_attr[3]
    key=(venue,batsman) # in tuple format

        #reformatting value
    value=value.split('\'')
    ctr=int(value[1]);
    runs=int(value[3]);

    if(key in result.keys()):
    {
        result[key][0]+=ctr;
        result[key][1]+=runs;
    }
    else:
    result.update({key:[ctr,runs]});
# removing all cases where n of deliveries is less than 10
for keys in result:
    if(result[keys][0]<10):
        del(result[keys]) # removing elements with less than 10 deliveries

for i in result:
    result[i]=[batsman,result[i][1]/result[i][0]] #total runs/ total deliveries
    i=venue
    print('%s:%s' % (str(i),str(result[i])))

# output format
#venue:[batsman,strikerate] 
