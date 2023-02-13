import os

import requests

db_path = "./docker/mysql/init/"
db_url = "http://ergast.com/schemas/f1db_tables.sql"

if os.path.exists("./docker/mysql/init/f1db.sql"):
    print(f"f1db.sql found in {db_path}")
    exit(0)

if not os.path.exists(db_path):
    print(f"Directory {db_path} not found, creating.....")
    os.makedirs(db_path)


print(f"Downloading f1db.sql to {db_path}")
res = requests.get(db_url)

print(f"Saving file f1db.sql to {db_path}/f1db.sql")
with open(db_path + "f1db.sql", "wb") as f:
    f.write(res.content)
