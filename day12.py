print("Catch up in Preview".center(80, "-"))

#How to import a module in other .py file
# import filename

import os
print(os.getcwd()) #Get current directory

print("random module")

from random import randint, random

print(random())
print(randint(5, 20))

import string  # noqa: E402

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print("Exercise 1".center(80, "-"))

import random
import string  # noqa: E402


def generate_user_id():
    random_id = "".join(random.choices(string.digits + string.ascii_letters, k=6))
    # Dont forget k=6 is inside the random function , dont put wrong ()
    return random_id


print(generate_user_id())

print("Exercise 2".center(80, "-"))


def used_id_gen_by_user(num_character, num_id):  # num_id = 5
    for i in range(0, num_id):  # 0,1,2,3,4
        ID = "".join(
            random.choices(string.digits + string.ascii_letters, k=num_character)
        )
        print(ID)


used_id_gen_by_user(16, 5)

print("Exercise 3".center(80, "-"))
print(
    "Write a function named rgb_color_gen. \nIt will generate rgb colors (3 values ranging from 0 to 255 each)."
)


def rgb_color_gen():
    return f"rgb({randint(0,256)}, {randint(0,256)}, {randint(0,256)})"
    # f'' String can be used as return result

print(rgb_color_gen())
# print()

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
"""
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""

def list_of_hexa_colors():
    populations = "abcdef0123456789"
    # print(random.choices(populations,k=6))
    hexa_color_code = "#" + "".join(random.choices(populations, k=6))
    return hexa_color_code

print(list_of_hexa_colors())

print("Exercise 2".center(80, "-"))

def list_of_rgb_colors(num_of_rgb_color):  # num_of_rgb_color = 5
    output = [
        f"rgb({randint(0,256)}, {randint(0,256)}, {randint(0,256)})"
        for i in range(0, num_of_rgb_color)
    ]
    return output

print(list_of_rgb_colors(4))

print("Exercise 3".center(80, "-"))
print(
    "Write a function generate_colors \nwhich can generate any number of hexa or rgb colors."
)


def list_of_hexa_colors(num_of_hexa_color):
    populations = "abcdef0123456789"
    # print(random.choices(populations,k=6))
    output = [
        f'{"#" + "".join(random.choices(populations, k=6))}'
        for i in range(0, num_of_hexa_color)
    ]
    return output

print(list_of_hexa_colors(4))

def generate_colors(hexa_or_rgb, num_of_color):
    if hexa_or_rgb == "hexa":
        return list_of_hexa_colors(num_of_color)
    else:
        return list_of_rgb_colors(num_of_color)

print(generate_colors("hexa", 3))
print(generate_colors("rgb", 6))

print("Exercise Level 3".center(80, "-"))
print("Exercise 1".center(80, "-"))
print(
    "Call your function shuffle_list, \nit takes a list as a parameter and it returns a shuffled list"
)

# x = ["ft", "pig", "fat"]
# x = list("abcdef")
# print(f"Before: {x =}")
# random.shuffle(x)
# print(x)


def shuffle_list(lst):
    random.shuffle(lst)
    return lst


print(shuffle_list(["ft", "pig", "fat"]))

print("Exercise 2".center(80, "-"))
print(
    "Write a function which returns an array of seven random numbers \nin a range of 0-9. All the numbers must be unique."
)


def random_numbers():
    random_num_set = set()
    while len(random_num_set) < 7:
        random_num_set.add(str(randint(0, 10)))
    # return ''.join(list(random_num_set))
    # if wanna return a string
    return list(random_num_set)  # if wanna return a list of numbers

print(random_numbers())
