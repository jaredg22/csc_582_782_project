#!/usr/bin/env python3

import sys
import json


i=0
for line in sys.stdin:
    if i > 0:
        # if i < 201:
        line.strip()
        line = line[:-2]
        valsDict = json.loads(line)
        if len(valsDict["sub_product"]) > 0:
            print('%s\t%s' % (valsDict["sub_product"], 1))
        else:
            print('%s\t%s' % ("No sub_product", 1))
    i+=1