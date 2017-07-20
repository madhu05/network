#!/usr/bin/python

from __future__ import print_function
import json
from cassandra.query import dict_factory
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('test1space')

session.row_factory = dict_factory
rows = session.execute("SELECT type, id, ip_address, alerts FROM mytable")
f = open('sample', 'w')
for row in rows:
    print(row, file=f)
data = json.load(open('/root/cassandra/sample'))
with open('result.json', 'w') as fp:
     json.dump(data, fp)
