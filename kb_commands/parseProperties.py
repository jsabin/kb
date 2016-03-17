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
table.set_cols_dtype(['t', 't'])
table.set_cols_align(["l", "l"])

properties = [["Name", "Value"]]
for service in decoded:
    if service['name'] == sys.argv[1]:

        for propertyName, property in service.items():
            if propertyName != "name" and propertyName != "svc_id" and propertyName != "environment_name" and propertyName != "type":
                for valueName, value in property.items():
                    if valueName != "environment_name":
                        properties.append([propertyName, value])
        break

table.add_rows(properties)
print(table.draw())
