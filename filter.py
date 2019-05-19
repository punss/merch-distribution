import rethinkdb as rdb
import os

r = rdb.RethinkDB()
conn = r.connect("192.168.0.102",28015).repl()

givlist = []
zero = r.table("null").filter({"ID":"2013A2PS0151H"}).run(conn)

while True:
    id = input("Enter the ID Number: ")
    names=r.table("tshirts").filter({"ID":id}).run(conn)
    tangible = names
    if (len(list(tangible))==0):
        print("No results.")
        continue
    duplist = []
    count = 1
    for person in names:
        else:
            duplist.append(person)
            print (str(count) +". " + person["ID"])
            count+=1
            # print (person["ID"])
            print (person["Name"])
            print ("Sizes ordered:")
            for size in person:
                if (
                    size=="XS" or size=="S" or size=="M" or size=="L"
                    or size=="XL" or size=="XXL" or size=="XXXL"
                    ):
                    # print (size)
                    if (int(person[size])>0):
                        print (size + ": " +person[size]+"\n")
    sub = int(input("Index of person given to: "))
    if sub==0:
        os.system('clear')
        print("Cancelled.")
        continue
    sub-=1
    r.table("submitted").insert(duplist[sub]).run(conn)
    r.table("tshirts").filter({"Name" : (duplist[sub]["Name"])}).delete().run(conn)
