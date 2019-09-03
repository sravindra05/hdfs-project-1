#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/python
import sys
import csv


# In[12]:


csv_input = sys.stdin
venue='' #initially empty string
#csv_input=r'C:\Users\USER i5\Downloads\alldata.csv'


# In[13]:


with open(csv_input,'rt')as f:
    data = csv.reader(f)
    for row_list in data:
        #print(row)
        # key,value : (Venue,Batsman),[no of deliveries,no of runs]
        # exclude cases with extras 
        # storing venue for each match
        #print(row_list)
        if(row_list[0]=='info' and row_list[1]=='venue'):
            venue=row_list[2]
            #print(venue+"\n")
        #recording values for each match, taking in only values which are not extras 
        elif(row_list[0]=='ball' and int(row_list[8])==0):
            key=(venue,row_list[4])
            val=[1] # no_of_deliveries for 1 record
            val.append(int(row_list[7])) # no_of_runs in record
            print('%s:%s' % (str(key),str(val)))
        else:
            continue


# In[ ]:




