import rethinkdb as rdb
import json
import sys

r = rdb.RethinkDB()
conn = r.connect("192.168.0.102",28015).repl()

with open(sys.argv[1],"r") as f:
    data = json.load(f)

r.db("test").table_create("tshirts").run(conn)
r.db("test").table_create("submitted").run(conn)
r.db("test").table_create("null").run(conn)
r.table("tshirts").insert(data).run(conn)
