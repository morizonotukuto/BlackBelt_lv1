import random

number = random.randint(1, 10)
loop = True

while loop:
    date = int(input("Guess the number: "))

    if date == number:
        print ("Correct!")
        loop = False

    else :
        print ("Wrong, try again! ")

