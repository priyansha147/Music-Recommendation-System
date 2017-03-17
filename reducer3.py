#!/usr/bin/python

import sys
import ast

last_key = None
last_val = []
for line in sys.stdin:
    if len(line.strip()) == 0: 
	#print 'yolo'
	continue
    input_dct = ast.literal_eval(line)
    val = input_dct.values()[0]
    key = input_dct.keys()[0]
    #print 'val',val
    if last_key != None and last_key!= key:
	song_sim = sorted(last_val,reverse=True, key=lambda x: x[1])
	last_val = val
	print {last_key:song_sim[0:10]} 
	
    else:
        last_val += val

    last_key = key
    #print 'val',val
    #print 'lval',last_val
    

#print last_key,key
if last_key == key:
    song_sim = sorted(last_val,reverse=True, key=lambda x: x[1])
    print {last_key:song_sim[0:10]}

    




