#!/usr/bin/python

# use TestTable
# pip install -U git+http://github.com/bufordtaylor/python-texttable or apt-get install python-texttable

import json
import sys

data = ''
for line in sys.stdin:
    data += line

decoded = json.loads(data)

for service in decoded:
    if service['environment_name'] == sys.argv[1]:
        print service['name']

