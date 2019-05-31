import rethinkdb as rdb
import os

IP = input("Enter the IP address: ")
r = rdb.RethinkDB()
conn = r.connect(IP, 28015).repl()

while True:
    id = input("Enter the ID Number: ")
    names = r.table("tshirts").filter({"ID": id}).run(conn)
    tangible = r.table("tshirts").filter({"ID": id}).run(conn)
    if (len(list(tangible)) == 0):
        print("No results.")
        continue
    duplist = []
    count = 1
    for person in names:
        duplist.append(person)
        print(str(count) + ". " + person["ID"])
        count += 1
        print(person["Name"])
        print("Sizes ordered:")
        for size in person:
            if (
                size == "XS" or size == "S" or size == "M" or size == "L" or
                size == "XL" or size == "XXL" or size == "XXXL"
                    ):
                # print (size)
                if (int(person[size]) > 0):
                    print(size + ": " + person[size]+"\n")
    sub = int(input("Index of person given to: "))
    if sub == 0:
        os.system('clear')
        print("Cancelled.")
        continue
    sub -= 1
    r.table("submitted").insert(duplist[sub]).run(conn)
    r.table("tshirts").filter(
        {"Name": duplist[sub]["Name"]}
        ).delete().run(conn)
