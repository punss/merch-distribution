import json

f = open("t.txt","r")
data = json.load(f)

givlist=[]
while True:
    id = input("Enter the ID Number: ")
    count = 0
    duplist=[]
    for person in range(len(data)):
        if id in data[person]["ID"]:
            count+=1
            flag = 1
            duplist.append(data[person])
            print (str(count) + ". " + data[person]["ID"])
            # print (data[person]["ID"])
            print (data[person]["Name"])
            print ("Sizes ordered:")
            for size in data[person]:
                if (
                    size=="XS" or size=="S" or size=="M" or size=="L"
                    or size=="XL" or size=="XXL" or size=="XXXL"
                    ):
                    # print (size)
                    if (int(data[person][size])>0):
                        print (size + ": " +data[person][size])

    if (count>0):
        dist = input("Given? ")
        if (dist == "Y" or dist == "y"):
            if (count == 1):
                givlist.append(duplist[0])
                data.remove(duplist[0])
            elif (count>1):
                ch = int(input("SNo. of person distributed to: "))
                if(ch in range(len(duplist)+1)):
                    givlist.append(duplist[ch-1])
                    data.remove(duplist[ch-1])
        else:
            duplist=[]
            continue

    if (flag==0):
        flag2 = 0
        for person in range(len(givlist)):
            if id in givlist[person]["ID"]:
                print("Items for this ID have already been distributed.")
                flag2 =1
        if (flag2 == 0):
            print("ID Number not found.")
    flag=0
