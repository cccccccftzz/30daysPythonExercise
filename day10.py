# Loops


print("Catch up in Preview".center(80, "-"))
print("While Loop".center(50, "-"))
count = 0
while count < 5:
    print(count)
    count = count + 1

print("while + else".center(50, "-"))
count = 0
while count < 6:
    print(count)  # 0,1,2,3,4,5
    count = count + 1  # 1,2,3,4,5,6
else:
    print(count)  # 6

count = 0
while count < 6:
    print(count)  # 0,1,2,3,4,5
    count = count + 1  # 1,2,3,4,5,6
print(count)  # 6
""" 
Under this case, giving else or not no difference
as long as the loop completed successfully.
see another case if the loop break in the mid way,
then else will be necessary
"""

print("while + if break + else".center(50, "-"))
count = 0
while count < 6:
    if count == 5:
        break  # Here once the loop break, it wont execute the else clause, either.
    print(count)  # 0,1,2,3,4
    count = count + 1  # 1,2,3,4,5
print(count)  # 5

count = 0
while count < 6:
    if count == 5:
        break
    print(count)  # 0,1,2,3,4
    count = count + 1  # 1,2,3,4,5
else:
    print(count)  # will not run this row

print("while + if continue + else".center(50, "-"))
count = 0
while count < 5:
    if count == 3:
        count = count + 1  # 4
        continue
    print(count)  # 0,1,2,4,
    count = count + 1  # 1,2,3,5

print("For Loop with string".center(50, "-"))
language = "python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
# All the loop result are automatically give a new line
"""
p
y
t
h
o
n
"""

print("For Loop with list".center(50, "-"))
lst = [1, 3, 5, 7, 9]
for element in lst:
    print(element)

print("For Loop with tuple".center(50, "-"))
for i in (0, 1, 2, 3, 4, 5):
    print(i)

print("For Loop with dictionary".center(50, "-"))
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
for key_of_person in person:
    print(key_of_person)

for key_value_of_person in person.items():
    print(key_value_of_person)

print("For Loop with set".center(50, "-"))
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)
# When using for loop for set, the loop result are not in order

print("For + if break ".center(80, "-"))
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

print("For + if continue ".center(80, "-"))
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print(
        "loop's end"
    )  # for short hand conditions need both if and else statements
print("outside the loop")

print("range () Function ".center(80, "-"))
lst = list(range(11))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = list(range(2, 6, 2))
print(lst)  # [2, 4]

print("nested for loop".center(80, "-"))
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

for key in person:
    if key == "skills":
        for every_skill in person["skills"]:
            print(every_skill)
            print(type(every_skill))

print("for + else ".center(80, "-"))
for number in range(4):
    print(number)  # 0,1,2,3
else:
    print("The loop ended")
""" 
Similarly, if no break the for loop 
giving else or not no difference
"""
print("for + break + else ".center(80, "-"))
for number in range(4):
    print(number)  # 0,1,2,3
    if number == 3:
        break
else:
    print("The loop ended")  # The else clause wont be executed since the loop break.

print("pass statement".center(80, "-"))
for number in range(5):
    pass

print("Exercise Level 1".center(80, "-"))
print("Exercise 1".center(80, "-"))
# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(0, 11):
    print(i)

"""
while i in range (0,11):
    print (i)

The main difference in while and for loop
when you are using while loop
the value of 'i' is not updated within the loop,
like this script, we have defined i before, i = 10
and i in range (0,11) are always True, 
leading to an infinite repetition of the same condition
"""
print(type(range(0, 11)))

i = 0
while i < 11:
    print(i)
    i += 1

print("Exercise 2".center(80, "-"))
# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, -1, -1):
    print(number)  # 10,9,8,...0

number = 10
while number >= 0:
    print(number)
    number = number - 1  # number -= 1

print("Exercise 3".center(80, "-"))
"""Write a loop that makes seven calls to print(), 
so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
for i in range(1, 8):
    print(i * "#")

number = 1
while number < 8:
    print(number * "#")
    number += 1  # Dont forget to give the iteration to update the value in while loop

print("Exercise 4".center(80, "-"))
"""
Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

for row in range(1, 9):  # row = 1,
    for row_member in range(1, 9):  # row_member = 1, 2, 7, 8
        if row_member == 8:
            print("#")
            break
        print("#", end=" ")  #

print("Exercise 5".center(80, "-"))
"""
Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for i in range(0, 11):
    print(f"{i} x {i} = {i*i}")

print("Exercise 6".center(80, "-"))
"""
Iterate through the list, 
['Python', 'Numpy','Pandas','Django', 'Flask'] 
using a for loop and print out the items
"""
# For loop with list
skills = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for i in skills:
    print(i)

print("Exercise 7".center(80, "-"))
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=" ")

print("\n")
print("Exercise 8".center(80, "-"))
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0, 101):
    if i % 2 == 1:
        print(i, end=" ")

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
"""
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
"""
sum = 0
for i in range(0, 101):
    sum += i
print(f"The sum of all numbers is {sum}")

print("Exercise 2".center(80, "-"))
"""
Use for loop to iterate from 0 to 100 
and print the sum of all evens and the sum of all odds.
The sum of all evens is 2550. And the sum of all odds is 2500
"""
sum_even = 0
sum_odd = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(
    f"The sum of all even numbers are {sum_even}. \nThe sum of all odd numbers are {sum_odd}."
)

print("Exercise Level 3".center(80, "-"))
print("Exercise 1".center(80, "-"))
"""
Go to the data folder and use the countries.py file. 
Loop through the countries 
and extract all the countries containing the word land
"""
file_path = "data/countries.py"
with open(file_path, "r") as file:
    script_content = file.read()

exec(script_content)  # Execute the script content
print(countries[30])

print("Method 1".center(60, "-"))
# Method 1 by using index iteration
print(len(countries))
countries_with_land = []
for i in range(0, len(countries)):
    if "land" in countries[i]:
        countries_with_land.append(countries[i])
print(countries_with_land)

print("Method 2".center(60, "-"))
# Method 2 by direct indices
countries_with_land = []
for country in countries:
    if "land" in country:
        countries_with_land.append(country)
print(countries_with_land)

print("Exercise 2".center(80, "-"))
"""
This is a fruit list, 
['banana', 'orange', 'mango', 'lemon'] 
reverse the order using loop.
"""
fruits = ["banana", "orange", "mango", "lemon"]
reverse_fruits = []
for fruit in fruits:
    reverse_fruits.insert(0, fruit)
print(reverse_fruits)

fruits = ["banana", "orange", "mango", "lemon"]
reverse_fruits = []
for fruit in reversed(fruits):  # reversed(list)
    reverse_fruits.append(fruit)
print(reverse_fruits)


print("Exercise 3".center(80, "-"))
"""
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
"""
file_path = "data/countries_data.py"
with open(file_path, "r", encoding="utf-8") as file:
    script_content = file.read()

exec(script_content)  # Execute the script content

print("Exercise 3.i".center(80, "-"))
total_number_of_languages = 0
list_of_language = []
for each_country in countries_data:
    list_of_language += each_country["languages"]

# What are the total number of languages in the data
print(
    len(set(list_of_language))
)  # Use the unique properties to count the total language numbers

print("Exercise 3.ii".center(80, "-"))
# Find the ten most spoken languages from the data
set_of_language = set(list_of_language)

"""
Method 1: create 2 lists then pairing by zip() 
To convert the set into list (to make every country in order)
list_set_of_language = list(set_of_language)
list_appearance_time_language = []
for every_language in list_set_of_language:
    n = list_of_language.count(every_language) # Rmr to quote the correct original list of full national language
    list_appearance_time_language.append(n)
print(list_appearance_time_language)
"""

# Method 2: straightly to create the dictionary
language_counts = {}
for language in set_of_language:
    language_counts[language] = list_of_language.count(language)
    # To create the pairing dictionary directly -> language:counts

"""
which method better? 
Method 1 or method 2?
Method 2 much easier and clearer and no need pay attention on the order initially
"""

list_appearance_time_language = list(language_counts.items())
list_appearance_time_language.sort(key=lambda x: x[1], reverse=True)
# To sort by the second element in the tuple, and descending

print("Top 10 most spoken languages:")
for language, count in list_appearance_time_language[:10]:
    print(f"{language}: {count}")

print("Exercise 3.iii".center(80, "-"))
# Find the 10 most populated countries in the world
country_population = {}  # Dont forget to create a empty dictionary
for each_country in countries_data:
    country_population[each_country["name"]] = each_country["population"]

print(country_population)
sort_by_value = lambda x: x[1]
list_populated_country = list(country_population.items())
list_populated_country.sort(key=lambda x: x[1], reverse=True)

print("Top 10 most populated countries in the world: ")
for country, population in list_populated_country[:10]:
    print(f"{country}: {population}")

print(sorted({1: "D", 2: "B", 13: "B", 8: "E", 4: "A"}))  # [1, 2, 4, 8, 13]
