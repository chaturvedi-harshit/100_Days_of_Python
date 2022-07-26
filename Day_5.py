# For Loops

from secrets import choice
import random
fruits = ["Apple", "Pear", "Peach"]

# for i in fruits:
#     print(i.upper())


# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# print(student_heights)

# student_count = 0
# sum = 0

# for height in student_heights:
#     sum += height
#     student_count += 1

# average_height = sum/student_count
# print(average_height)


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)


# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score


# print(highest_score)


# Range

# Syntax
# for i in range(a,b):
#     print(i)


# for i in range(len(fruits)):
#     print(i, fruits[i])
#     fruits[i] = "Hola"

# print(fruits)


# sum = 0

# for number in range(2, 101, 2):
#     sum += number

# print(sum)


# Fizzbuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print(number, "Fizz")
    elif number % 5 == 0:
        print(number, "Buzz")
    else:
        print(number)


# Password Generator

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password = []
no_of_letters = random.choices(letters, k=nr_letters)
password.extend(no_of_letters)

no_of_numbers = random.choices(numbers, k=nr_numbers)
password.extend(no_of_numbers)

no_of_symbols = random.choices(symbols, k=nr_symbols)
password.extend(no_of_symbols)

random.shuffle(password)

final_password = ""
for item in password:
    final_password += item


print(final_password)


# password2 = ""

# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password2 += random_char
#     print(password2)
