#!/usr/bin/env python
import json
import logging

log = logging.getLogger()
log.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "test1space"

def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    rows = session.execute("SELECT keyspace_name FROM system.schema_keyspaces")
    if KEYSPACE in [row[0] for row in rows]:
        log.info("dropping existing keyspace...")
        session.execute("DROP KEYSPACE " + KEYSPACE)

    log.info("creating keyspace...")
    session.execute("""
        CREATE KEYSPACE %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % KEYSPACE)

    log.info("setting keyspace...")
    session.set_keyspace(KEYSPACE)

    log.info("creating table...")
    session.execute("""
        CREATE TABLE mytable (
        type text,
        id text,
        alerts text,
        imageSrc text,
        ip_address text,
        imageSize text,
        mac_address text,
        PRIMARY KEY (ip_address)
        )
        """)

    query = SimpleStatement("""
        INSERT INTO mytable (type, id, alerts, imageSrc, ip_address, imageSize, mac_address)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, consistency_level=ConsistencyLevel.ONE)


    prepared = session.prepare("""
        INSERT INTO mytable (type, id, alerts, imageSrc, ip_address, imageSize, mac_address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """)

    json_obj = json.load(open('/root/sample.json'))

    for product in json_obj["network"]["nodes"]:
        session.execute(query, (str(product["type"]), str(product["id"]),str(product["properties"]["alerts"]),str(product["properties"]["imageSrc"]),str(product["properties"]["ip_address"]),str(product["properties"]["imageSize"]),str(product["properties"]["mac_address"])))



    future = session.execute_async("SELECT * FROM mytable")
    log.info("type\id\alerts\imageSrc\ip_address\imageSize\mac_address")
    log.info("---\t----\t----")

    try:
        rows = future.result()
    except Exception:
        log.exeception()

    for row in rows:
        log.info('\t'.join(row))

    #session.execute("DROP KEYSPACE " + KEYSPACE)

if __name__ == "__main__":
    main()
