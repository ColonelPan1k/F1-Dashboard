import gzip
import os
import shutil

import requests

db_path = "./docker/mysql/init"
db_url = "http://ergast.com/downloads/f1db.sql.gz"

if os.path.exists("./docker/mysql/init/f1db.sql"):
    print(f"f1db.sql found in {db_path}")
    exit(0)

if not os.path.exists(db_path):
    print(f"Directory {db_path} not found, creating.....")
    os.makedirs(db_path)


print(f"Downloading f1db.sql to {db_path}")
res = requests.get(db_url)


print(f"Saving file f1db.sql.gz to {db_path}/f1db.sql.gz")
with open(f"{db_path}/f1db.sql.gz", "wb") as f:
    f.write(res.content)

print(f"Extracting file f1db.sql to {db_path}/f1db.sql")
with gzip.open(f"{db_path}/f1db.sql.gz", "rb") as f_in:
    with open(f"{db_path}/f1db.sql", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
