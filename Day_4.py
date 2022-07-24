import random


number = random.randint(0, 1)
# print(number)


# if number == 1:
#     print("Heads")
# else:
#     print("Tails")


# Lists
states = ["UP", "Punjab", "Rajasthan"]

# print(states[0])

states[0] = "Balle Balle"
# print(states[0])

states.append("Kanpur")


states.insert(0, "0 index per aise append kar sakte hain")


states.extend(["This is an extended list"])

states.pop()

# print(states)


# Short excercise

names_string = input(
    "Type in names of all the people separated with commas: ")

names = names_string.split(",")

print(names)


# Both of the below are right. Uncommenting the one I wrote first.
# print(names[random.randint(0, len(names))])
print(f"{names[int(random.random()*len(names))]} is going to buy the dinner")


# Short excercise
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])  # 2
vertical = int(position[1])  # 3

map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# Rock, Paper and Scissors Game Small Project

game_choices = ["Rock", "Paper", "Scissors"]

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

if user_input >= 3:
    print("Please enter valid number")

user_choice = game_choices[user_input]

print(user_choice)

computer_choice = random.choice(game_choices)
print(computer_choice)


if user_choice == "Rock" and computer_choice == "Paper":
    print("You lose")
if user_choice == "Rock" and computer_choice == "Scissors":
    print("You win")
if user_choice == "Rock" and computer_choice == "Rock":
    print("It's a draw")
if user_choice == "Paper" and computer_choice == "Rock":
    print("You win")
if user_choice == "Paper" and computer_choice == "Scissors":
    print("You lose")
if user_choice == "Paper" and computer_choice == "Paper":
    print("It's a draw")
if user_choice == "Scissors" and computer_choice == "Rock":
    print("You lose")
if user_choice == "Scissors" and computer_choice == "Paper":
    print("You win")
if user_choice == "Scissors" and computer_choice == "Scissors":
    print("It's a draw")
elif user_input >= 3:
    print("Please enter valid number")
