#!/usr/bin/python

# use TestTable
# pip install -U git+http://github.com/bufordtaylor/python-texttable or apt-get install python-texttable

import json
import sys
from texttable import Texttable

data = ''
for line in sys.stdin:
    data += line

decoded = json.loads(data)

table = Texttable(132) # Set max_width to infinite
table.set_deco(Texttable.HEADER)
table.set_cols_dtype(['t', 't', 't', 't', 't', 't'])
table.set_cols_align(["l", "l", "l", "l", "l", "l"])

machines = [["Name", "IP", "Status", "Roles", "Environment", "JSON Tags"]]
count = 0
for machine in decoded:
    machines.append([machine['fqdn'], machine['ip_address'], machine['status'], machine['roles'], machine['environment_name'], machine['tags']])
    count += 1

table.add_rows(machines)
print(table.draw())

print "Total %d" % count