# Variable

print("A) built-in functions")

print(abs(5 + 6j))  # why the returned value is 7.81?
print(abs(-5.65))

print(bool([]))
print(bool(0))
print(bool(""))
print(bool(None))

print(len("hello, world!"))
print(type("hello, world"))
print(type(str(10)))  # Concert interger into string type '10'
print(type(int("10")))  # Convert string into interger type
# input('enter your name:')

print(max(20, 30, 40, 50))
print(min(20, 30, 40, 50))
print(min([20, 30, 40, 50]))
"""
Line 20: the [] is ONE argument 
sometimes it has been alr defined in one list before, so no need list down different argument.
"""
print(sum([20, 50]))

print('\nB) Invalid Variable  Name: "-". Start with Number, Special figure like @$%')

print("\nC) Viarables in Python")
first_name = "Fang Ting"
last_name = "Chen"
country = "China"
age = "30"
is_married = False
skills = ["gym", "structural design", "python"]
person_info = {
    "first_name": "Fang Ting",  # Dont forget to give ","
    "last_name": "Chen",
    "country": "China",
    "age": "30",
    "is_married": False,
}

print("Exercise Level 1".center(50, "-"))
print(type(person_info))
print(type("person_info"))  # When it comes with '' meaning it is a string purely

print("First Name:", first_name)
print("First Name Length", len(first_name))
print("Last Name:", last_name)
print("Last Name Length", len(last_name))
print("\n")  # how to insert a new line when printing the multiple variables
print(first_name, last_name, age, country, is_married, skills)

# last_name = input("What is your Last name:")
# age = input("How old are you?")
print(last_name)
print(age)
print("\n\n\n")
print("\t", age)
print(len("\t"), age)
print(
    type(zip([1, 2], [3, 4]))
)  # zip function - to match each argument according to the order
print((zip([1, 2], [3, 4])))
print(list((zip([1, 2], [3, 4]))))

num_int = 10
num_flo = float(num_int)
print(f"{num_flo:.2f}")

num_flo = 5 / 3
print(f"{num_flo:.4f}")

print(int(num_flo))

print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

a, b, c = 1, 5, 3
print(a, b)
print(c)
a, b, c = (10, 20, 30)
print(a, b, c)
a, b, c = a, c, b
print(a, b, c)

print("Exercise Level 2".center(50, "-"))
# print('Exercise Level 2\n',"-" * 50)

print("Exercise Level 2.2 & 2.3".center(35, "~"))
length_first_name = len(first_name)
length_last_name = len(last_name)
print(length_first_name > length_last_name)

print("Exercise Level 2.4".center(35, "~"))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two  # 取余数
exp = num_one**num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

print("Exercise Level 2.5".center(35, "~"))
radius_circle = int(input("Please enter the radius of the circle = "))
import math  # math.pi

area_of_circle = math.pi * (radius_circle**2)
print(f"{area_of_circle = :.2f}")
print(
    f"{area_of_circle  =      }"
)  # Only to show the space to be printed accordingly when using f""
circum_of_circle = math.pi * (radius_circle * 2)
print(f"{circum_of_circle = :.2f}")

print("Exercise Level 2.6".center(35, "~"))
last_name = input("What is your Last name?")
fist_name = input("What is your First name?")
age = input("How old are you?")
city = input("Which city are you from?")
print(last_name)
print(fist_name)
print(age)
print(city)

# print('Exercise Level 2.7'.center(35, "~"))
# help('async')

print("Exercise Level 2.7".ljust(35, "~"))
print("Exercise Level 2.7".rjust(35, "~"))
