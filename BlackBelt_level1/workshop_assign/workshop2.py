import json

with open('workshop.json', 'r') as f:
    data = json.load(f)

while (True):
   
    state = input("Please Enter add for add a birthday or find for find a birthday :")

    if (state == "add" ):

        name = input("Pass Enter name : ")
        bir = input("Pass Enter birthday : ")

        data[name] = bir
        with open('workshop.json', 'w') as f:
           json.dump(data, f)


    elif (state == "find" ):
        print ("Welcome to the birthday dictionary. We know the birthdays of: ")
        for i in data["birthday"]:
            print (i["name"])
        
        
        name = input("Who's birthday do you want to look up?")

        for i in data["birthday"]: 
           if (name == i["name"]):
               print (i["birthdays"])

