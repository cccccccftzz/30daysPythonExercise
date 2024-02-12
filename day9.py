# Conditionals

print("Catch up in Preview".center(80, "-"))

print("Exercise 1".center(80, "-"))
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-user_age} more years to learn to drive")

print("Exercise 2".center(80, "-"))
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 30
your_age = int(input("Enter your age: "))
age_difference = your_age - my_age
if age_difference >= 0:
    if age_difference > 1:
        print(f"Your age is {age_difference} years older than me.")
    elif age_difference == 1:
        print("Your age is one year older than me.")
    else:
        print("your age is the same as mine")
else:
    if age_difference < -1:
        print(f"Your age is {-age_difference} years younger than me.")
    else:
        print("Your age is one year younger than me.")


print("Exercise 3".center(80, "-"))
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
differece = number_one - number_two
if differece > 0:
    print(f"{number_one} is greater than {number_two}")
elif differece < 0:
    print(f"{number_one} is smaller than {number_two}")
else:
    print(f"{number_one} is equal to {number_two}")

print("Exercise Levek 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
student_score = int(input("Enter the student score: "))
if student_score > 100:
    grade = "Invalid Score!"
elif 90 <= student_score <= 100:
    grade = "A"
elif student_score >= 70:
    grade = "B"
elif student_score >= 60:
    grade = "C"
elif student_score >= 50:
    grade = "D"
else:
    grade = "F"
print(grade)

print("Exercise 2".center(80, "-"))
season_for_checking = input("Enter the month: ")
captialize_season_for_checking = season_for_checking.capitalize()
autumn = {"September", "October", "November"}
winter = {"December", "January", "February"}
spring = {"March", "April", "May"}
summer = {"June", "July", "August"}

if captialize_season_for_checking in autumn:
    print("The season is autumn")
elif captialize_season_for_checking in winter:
    print("The season is winter")
elif captialize_season_for_checking in spring:
    print("The season is spring")
elif captialize_season_for_checking in summer:
    print("The season is summer")
else:
    print("Input wrong!")

print("Exercise 3".center(80, "-"))
fruits = ["banana", "orange", "mango", "lemon"]
fruits_input = input("Enter a fruit: ")
if fruits_input in fruits:
    print(f"The fruit {fruits_input} has already exist in the list")
else:
    fruits.append(fruits_input)
    print(fruits)

print("Exercise Level 3".center(80, "-"))
print("Exercise 1".center(80, "-"))
person = {
    "first_name": "Fang Ting",
    "last_name": "Chen",
    "age": 30,
    "Country": "China",
    "is_married": False,
    "skills": ["React", "Node", "Python"],  # Dictionary can store list
    "address": {
        "street": "Beach Road",
        "zipcode": "500045",
    },  # Dictionary can store subdictionary
}

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "Country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

if "skills" in person:
    length_skills = len(person["skills"])
    print(
        f'The middle skill of the person is {person['skills'][int (length_skills/2)]}'
    )
    print(
        f'The person {'has' if 'Python' in person['skills'] else 'has not'} the Python skill'
    )

""" If a person skills has only JavaScript and React, 
print('He is a front end developer')
if the person skills has MongoDB, Node, Python,
print('He is a backend developer'), 
if the person skills has MongoDB, Node, React,  
Print('He is a fullstack developer'), 
else print('unknown title') 
"""
if "skills" in person:
    if "MongoDB" in person["skills"]:
        if "Node" in person["skills"] and "React" in person["skills"]:
            print("He is a fullstack developer")
        elif "Node" in person["skills"] and "Python" in person["skills"]:
            print("He is a backend developer")
        elif "JavaScript" in person["skills"] and "React" in person["skills"]:
            print("He is a frontend developer")
    elif "JavaScript" in person["skills"] and "React" in person["skills"]:
        print("He is a frontend developer")
    else:
        print("Unknow title!")

"""If the person is married and if he lives in Finland, 
print the information in the following format:
Asabeneh Yetayeh lives in Finland. He is married.
"""
if person["is_married"] == True and person["Country"] == "Finland":
    print(
        f'{person['first_name']} {person['last_name']} lives in Finland. He is married. '
    )
elif person["is_married"] == True:
    print(
        f'{person['first_name']} {person['last_name']} does not in Finland. He is married. '
    )
else:
    print(
        f'{person['first_name']} {person['last_name']} does not in Finland. He/she is not married. '
    )


print("Exercise 4 method 2".center(80, "-"))

if "skills" in person:
    skills_list = person["skills"]
    if set(skills_list) == {"JavaScript", "React"}:
        print("He is a front end developer")
    elif set(skills_list) == {"Node", "Python", "MongoDB"}:
        print("He is a backend developer")
    elif set(skills_list) == {"React", "Node", "MongoDB"}:
        print("He is a fullstack developer")
    else:
        print("Unknown title")
else:
    print("Person dictionary does not have 'skills' key.")
print(skills_list)
