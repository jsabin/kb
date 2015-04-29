#!/usr/bin/python

import json
import sys

data = ''
for line in sys.stdin:
    data += line

if len(data) < 1:
    print "No data returned"
    sys.exit(1)

decoded = json.loads(data)

for machine in decoded:
    type = machine['tags']
    if not type:
        type = machine['roles']
    print "%s %s %s %s" % (machine['fqdn'], machine['environment_name'], machine['cloud'], type)
