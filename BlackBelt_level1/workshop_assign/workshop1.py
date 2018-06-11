birthday ={
    "Ada Lovelace" : "26/11/1985",
    "Albert Einstein" : "9/12/1985",
    "Benjamin Franklin" : "16/2/1989",
}

print ("Welcome to the birthday dictionary. We know the birthdays of: ")
for name in birthday:
    print (name)

name = input("Who's birthday do you want to look up?")
if name in birthday:
    print (name +"'s birthday is "+birthday[name])