import rethinkdb as rdb
import json
import sys

if len(sys.argv) < 3:
    print("Use python3 maketable.py <ip address> </path/to/tshirt.txt/>")
    exit(0)

r = rdb.RethinkDB()
conn = r.connect(sys.argv[1], 28015).repl()

with open(sys.argv[2], "r") as f:
    data = json.load(f)

r.db("test").table_create("tshirts").run(conn)
r.db("test").table_create("submitted").run(conn)
r.db("test").table_create("null").run(conn)
r.table("tshirts").insert(data).run(conn)
