
import os
import datetime
from datetime import date
from datetime import datetime
year = str(date.today().year)+" "
today = str(date.today())

today = datetime.strptime(today, "%Y-%m-%d")

birthday = {}
try:
    f = open("birthday.txt", "r")
except FileNotFoundError:
    f = open("birthday.txt", "w+")
    f.close()
    f = open("birthday.txt", "r")
    

for lines in f:
    birthday[lines.split(" - ")[0]] = lines.split(" - ")[1]

f.close()
name = " "
while True:
    name = input("\nWho are you interested in?\n").capitalize()
    if name in birthday:
        print("\nBirthday on")
        print(birthday[name])
    elif name == "":
        break
    else:
        print("{} not in a database".format(name))
        date = input("When is her/his birthday?\n")
        if date == "":
            print("{} not added.".format(name))
            continue
        else:
            print("{} added successfully to the database.".format(name))
        birthday[name] = date
        
        output = open("birthday.txt","a")
            
        output.write(name + " - " + date + "\n")
        output.close()
        #print("Birthday", end=" ")
    #date = year + birthday[name].strip()
    #date = datetime.strptime(str(date), "%Y %d %b")
    #print("in\n")
    #print(date - today)
    print("\n")

        

