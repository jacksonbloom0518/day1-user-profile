# program says welcome and my name
my_name = "Jackson"
print("Hello my name is " + my_name + "!")

print("Hello world!")

# string surround with either "" or ''. quotes don't matter

print("Jackson Bloom")

# Variables assigned with = . Cant have spaced or symbols besides _ or begin with #

meal = "shake"
print(meal)
meal = "pizza"
print(meal)
meal = "coffee"
print(meal)

# ERROR TYPES:
# 1. Syntax - something is wrong with written. punctuation missing, missing parenthesis
# 2. Name - sees word it doesn't recognize

# NUMERIC DATA TYPES
# 1. Int - whole number with not decimal point
# float - decimal point
release_year = 2025
runtime = 70
rating_out_of_ten = 9.5

# string lesson
favorite_word = "bussy"
print(favorite_word)

#string can be though of like lists
my_name = "Jackson"
first_initial = my_name[0]

# can slice a string with [_:_] will cut right before it
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
print(new_account)
temp_password = last_name[3:6]
print(temp_password)
# REVIEW WHERE IT STARTS AND STOPS

# Can concate strings with +
first_name = 'joey'
last_name = 'chang'
#REVIEW THIS FUNCTION
def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:3]
    return account_name

print(account_generator(first_name, last_name))

# len() will give you the length of each string
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
    account_name = first_name[len(first_name)-3:len(first_name)] + last_name[len(last_name)-3:len(last_name)]
    return account_name

temp_password = password_generator(first_name, last_name)
print(temp_password)

# negative indices will give you the last ex: -1 will give you last letter
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last_word = company_motto[-2]
final_word = company_motto[-4:]
print(final_word)

# strings aer IMMUTABLE (CANT BE CHANGED)... can use string to make others, but cant change string itslef
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]
print(first_name)

# add \ in front of special chars ("&') in order to use them
password = "theycallme\"crazy\"91"
print(password)

# iterating through loops
def get_length(word):
    size = 0
    for letter in word:
        size += 1
    return size
print(get_length('jackson'))

total = 1 + 2 +\
3 + 4 + 5
print(total)

is_valid = False
print(is_valid)
# DAY 1 PROJECT: MINI USER PROFILE GENERATOR

name = input("What is your name? ")
age = input("What is your age? ")
favorite_food = input ("What is your favorite food? ")
GPA = input("What is your GPA? ")
HOBBIES = input("what are your 2 favorite hobbies? ")

print("=== USER PROFILE ===")
print("Name: " + name.upper())
print("Age: " + age)
print("Favorite Food: " + favorite_food.lower())
print("GPA: " + GPA)
print("Hobbies: " + HOBBIES.lower())

