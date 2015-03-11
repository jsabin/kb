#!/usr/bin/python

import json
import sys

data = ''
for line in sys.stdin:
    data += line

decoded = json.loads(data)

for machine in decoded:
    type = machine['tags']
    if not type:
        type = machine['roles']
    print "%s %s %s %s" % (machine['fqdn'], machine['environment_name'], machine['cloud'], type)
