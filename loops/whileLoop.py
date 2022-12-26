import random
from math import sqrt

# While Loop

count = 0

while count < 9:
    print(" Number : ", count)
    count = count + 1

print("Good Bye")
# Making use of while loop to create a number guessing game

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else: 
        print("Sorry that you'er giving up")
        break
else: 
    print("Congratulation. You made it!")

# nested loops

print("Welcome to iron Bank of Bravoos ATM")
restart = "Y"
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input("please Enter Your 4 Digit Pin"))
    if pin == (1234):
        print("You entered your pin correctly\n")
        while restart not in ("n","No","no","N"):
            print("please Press 1 For Your Balance\n") 
            print("please Press 2 To Make withdraw\n") 
            print("please Press 3 To Pay in\n") 
            print("please Press 4 To Return Card\n")
            option = int(input("What Would you like to choose"))
            if option == 1:
                print("Your Balance is $",balance,"\n")
                restart = input("Would you like to go back")
                if restart in ("n","No","no","N"):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input("How Much Would you like to withdraw? \n$10/$20/$40/$60/$80/$100"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance = balance - withdrawl
                    print("\nYour Balance is now $", balance)
                    restart = input("would you like to go back? ")
                    if restart in ("n","No","no","N"):
                        print("Thank You")
                        break
                elif withdrawl != [10,20,40,60,80,100]:
                    print("Invalid Amount, PLease re-try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Please enter Desired amount"))
            elif option == 3:
                Pay_in = float(input("How Much Would you like to pay in? "))
                balance = balance + Pay_in
                print("\n Your Balance is now $", balance)
                restart = input("would you like to go back?")
                if restart in ("n","No","no","N"):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait whilist your card is Returned...\n")
                print("Thank you for you service")
                break
            else:
                print("Please Enter a correct number. \n")
                restart("y")
    elif pin != ("1234"):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\n more tries")
            break
