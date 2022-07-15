# Control Flow and Operators

# print("Welcome to the Rollercoaster!")

height = float(input("What is your height in cm? "))

if height >= 120:
    print("Let's ride the rollercoaster!")
else:
    print("Oops! Sorry, you have to grow taller than 120cm")

# Comparison Operator

# >
# <
# >=
# <=
# ==
# !=

# Let's do a simple odd or even number challange. Find if the number is even or odd

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("The number is an even number")
else:
    print("The number is an odd number")

# Nested if statements and elif statements

if height >= 120:
    print("Let's ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Pleas pay $12")
else:
    print("Oops! Sorry, you have to grow taller than 120cm")


# BMI excercise: Use control flow to display message according to the BMI

# Messages
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


height_two = float(input("What is your height in m? "))
weight = float(input("What is your weight in kgs? "))

bmi = round(weight/height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Excercise: Check if the year is a leap year

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4

# **except** every year that is evenly divisible by 100

# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)


year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("Not leap year.")


# Excercise:
# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0


if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill} ")


# Excercise:
your_name = input("What is your name? ").lower()

partner_name = input("What is their name? ").lower()


combine_name = your_name + partner_name


t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")


l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


# Project:
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


reply = input(
    "You are at a crossroad. Where do you want to go? Type \"left\" or \"right\".\n ").lower()


if reply == "left":
    reply2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n ").lower()

    if reply2 == "wait":
        reply3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()

        if reply3 == "red":
            print("It's a room full of fire. Game Over.")
        elif reply3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif reply3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You've fallen into a hole. Game Over")
