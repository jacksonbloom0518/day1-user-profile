# PYTHON CONDITIONALS AND IF STATEMENTS
# == EQUALS != NOT EQUALS >= GREATER OR EQUAL
from doctest import run_docstring_examples

a = 201
b = 200
c = 40
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b and a > c:
    print("a is the largest number")

if c < a or c < b:
    print("c isn't the largest number")
if not a < b:
    print("a is not less than b")
if a > 200:
    print("a is greater than 200")
    if a > 300:
        print("a is greater than 300")
    else:
        print("but less than 300")

if a > c :
    pass

x = 5
y = 10
z = 15

x *= 2
print(x)
print(x is y)
# CONDITIONS CHALLENGE
"""
temp = int(input("enter weather?"))
if temp >= 85:
    print("Wear shorts and a tank top!")
elif temp >= 60:
    print("Wear jeans and a t-shirt!")
else:
    print("Wear a jacket or sweater!")

# COMPARISON OPERATORS CHALLENGE
grade = int(input("enter your grade: "))
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# nested conditional
age = int(input("enter your age: "))
if age >= 12:
    have_ticket = input("Do you have a ticket? (yes/no): ")
    if have_ticket == "yes":
        print("Enjoy the ride")
    elif have_ticket == "no":
        print("you have to pay")
    else:
        print("please enter yes or no")
else:
    print("you are not old enough to ride")

# ternary operators
age = int(input("enter your age: "))
price = 10 if age < 18 else 20
print(price)

num = int(input("enter a number: "))
print("even") if num % 2 == 0 else print("odd")
"""
# FOR LOOPS
for x in range(6):
    print(x)
for x in range(2,30,3):
    print(x)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# LoOP Challenge : find fist even number

numbers = [1, 3, 7, 8, 5, 12, 3, 17, 38]

for x in numbers:
    if x % 2 == 0:
        print(x)
        break
    else:
        continue
        

# PYTHON PROJECT GUESS THE RANDOM NUMBER

import random
computer_number = random.randint(1,100)
guess_count = 0
guess_limit = 7
wins = 0
losses = 0
play_game = True
while play_game == True:
    computer_number = random.randint(1, 100)
    for i in range(7):
        print("You have " + str(guess_limit - i) + " guesses left.")
        num_guess = int(input("Guess a number between 1 and 100: "))
        if num_guess == computer_number:
            print("Correct!!! You win!")
            wins += 1
            play_game = bool(int(input("type 1 to play again or 0 to quit: ")))
            break
        elif num_guess < computer_number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        losses += 1
        print("Sorry, you ran out of guesses. The number was " + str(computer_number))
        play_game = bool(int(input("type 1 to play again or 0 to quit: ")))

print("You won " + str(wins) + " times and lost " + str(losses) + " times.")