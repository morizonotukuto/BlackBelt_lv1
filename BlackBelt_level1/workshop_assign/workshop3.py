import json
from collections import Counter
with open('workshop.json') as f:
    data = json.load(f)

diction = []
month = []
monthname = []
    

for i in range (len(data["birthday"])):
    month.append(data["birthday"][i]["birthdays"].split("/"))

for i in range (len(month)):
    diction.append(month[i][1]) 
    

for i in range (len(diction)):
    if int(diction[i]) == 1:
        monthname.append('January')
    elif int(diction[i]) == 2:
        monthname.append('February')        
    elif int(diction[i]) == 3:
        monthname.append('March')
    elif int(diction[i]) == 4:
        monthname.append('April')
    elif int(diction[i]) == 5:
        monthname.append('May')        
    elif int(diction[i]) == 6:
        monthname.append('June')
    elif int(diction[i]) == 7:
        monthname.append('July')
    elif int(diction[i]) == 8:
        monthname.append('August')        
    elif int(diction[i]) == 9:
        monthname.append('September')
    elif int(diction[i]) == 10:
        monthname.append('October')
    elif int(diction[i]) == 11:
        monthname.append('November')
    elif int(diction[i]) == 12:
        monthname.append('December')
    print (monthname[i])
 
    for x in data["birthday"]:
        if (diction[i]== x["birthdays"].split("/")[1]):
            print ("Name :"+x["name"])

