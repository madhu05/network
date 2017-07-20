import json
from sqlalchemy import create_engine
import MySQLdb

cursor = create_engine('mysql+mysqldb://root:Admin@localhost')
cursor.execute("USE test")
cursor.execute("""CREATE TABLE IF NOT EXISTS t10(
   type varchar(100) NOT NULL,
   id varchar(255) NOT NULL,
   alerts varchar(4) NOT NULL,
   imageSrc varchar(20) NOT NULL,
   ip_address varchar(20) NOT NULL,
   imageSize int(11) NOT NULL,
   mac_address varchar(20))""")
json_obj = json.load(open('/root/sample.json'))
for product in json_obj["network"]["nodes"]:
        cursor.execute("INSERT INTO t10 (type, id, alerts, imageSrc, ip_address, imageSize, mac_address) VALUES (%s,%s,%s,%s,%s,%s,%s)", (product["type"], str(product["id"]),product["properties"]["alerts"],product["properties"]["imageSrc"],product["properties"]["ip_address"],product["properties"]["imageSize"],str(product["properties"]["mac_address"])))
