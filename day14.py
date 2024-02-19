# higher order function

print("Catch up in Preview".center(80, "-"))
print("Function as a Parameter".center(80, "-"))


def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 3, 5])
print(result)

print("Function as a Return Value".center(80, "-"))


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= -0:
        return x
    else:
        return -x


def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute


result = higher_order_function(
    "square"
)  # result refer to one function, but function need take one argument
print(result(5))
result = higher_order_function("cube")
print(result(3))
result = higher_order_function("absolute")
print(result(-6))

print("Python Closures".center(80, "-"))


def add_ten():
    ten = 10

    def add(num):
        return (
            num + ten
        )  # ten is defined outside this function but within elsoing function

    return add


closure_result = add_ten()
print(closure_result(5))

print("Python Decorators".center(80, "-"))


def greeting():
    return "Welcome to Python"


def uppercase_decorator(function):
    def wrapper():
        func = function()
        # Typical format a = f() when using a variable to refer to a function
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())  # Here since "g" refers to one function, so need input one '()'

print("To implement the example above with a decorator")


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())

print("Applying Multiple Decorators to a Single Function")


# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Second Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        make_spilt = func.split()  # Split can use for function?!
        return make_spilt

    return wrapper


"""
1. The decorators closer to the function definition are applied first.
bc the .upper() does not work to list type
so cannot put uppercase wrapper later i.e. first 
2. The comment cannot put directly below the wrapper
"""


@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"


print(greeting())

print("Accepting Parameters in Decorator Functions")


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print(f"I live in {para3}")
    return wrapper_accepting_parameters

@decorator_with_parameters  # Wrapper will auto start with a new line
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach")

print(print_full_name("FT", "Chen", "Singapore"))

'''
I am FT Chen. I love to teach
I live in Singapore
'''

print("Built-in Higher Order Functions")
print("map ()")  # Takes a function and iterable as paramters
# Example 1
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


number_squared = map(square, numbers)
print(list(number_squared))

# Example 1 - lambda
# Try to lambda to simplify the function definition
number_squared = map(lambda a: a**2, numbers)
print(list(number_squared))

# Example 2
number_str = ["1", "2", "3", "4", "5"]
numbers_int = map(int, number_str)
print(
    numbers_int
)  # bc the numbers_int refer to a function, so the result will looks 0x0000
print(list(numbers_int))  # Can convert the list of strings into a list

number_str = ["1", "2", "3", "4", "5"]
numbers_int = map(int, number_str)
print(
    tuple(numbers_int)
)  # Can convert the list of strings into a tuple as well similarly

# Example 2
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased = map(lambda a: a.upper(), names)
print(list(names_upper_cased))

print("filter ()")  # calls the specified function which returns boolean for each item
numbers = [1, 2, 3, 4, 5]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(list(filter(is_even, numbers)))

print("reduce()")
from functools import reduce

"""
The reduce function applies this function cumulatively 
to the numbers in the list, 
resulting in the product of all the numbers.
"""
numbers_str = ["1", "2", "3", "4", "5"]


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, number_str)
print(total)  # 1+2+3+4+5=15

numbers_str = ["1", "2", "3", "4", "5"]


def mutiple_two_nums(x, y):
    return int(x) * int(y)


product = reduce(mutiple_two_nums, number_str)
print(product)  # 1*2*3*4*5=120


print("Exercise 1".center(80, "-"))
# Explain the difference between map, filter, and reduce.
"""
map: To execute the function to every member in the list and output a list
filter: To execute the conditional to every member and only return the member after filter with True result
reduce: To execute the function to every member cumulatively and only output one final result
"""

print("Exercise 2".center(80, "-"))
# Explain the difference between higher order function, closure and decorator
"""
higher order function: function can be as a parameter or function as a return value
python closures: Inside a nested function, can access a function within the closing function but outer scope
python decorators: To modify the function result without modifing the original function by writing a small function to define the pattern
"""

print("Exercise 3".center(80, "-"))
print("Define a call function before map, filter or reduce, see examples.")


def call_function(type):
    if type == "map":
        return map
    elif type == "filter":
        return filter
    elif type == "reduce":
        return reduce


number_str = ["1", "2", "3", "4", "5"]


def add_two_nums(x, y):
    return int(x) + int(y)


def is_even(num):
    if num % 2 == 0:
        return True


print("map")
result = call_function("map")  # Must read as a string with ''
print(
    list(result(int, number_str))
)  # Dont forget to use the list() to print out the map result
result_list = list(result(int, number_str))
print(result_list)

print("filter")
result = call_function("filter")
print(list(result(int, number_str)))
"""
In this code:

1. call_function('filter'): This returns the built-in filter function.
2. result(int, number_str): This applies the int function to each element in number_str, converting each string to an integer.
3. list(result(int, number_str)): This converts the result to a list.
4/ Here, the filter function is not actually used for filtering based on a condition. 
Instead, it's used as a placeholder for the map function, 
as returned by the call_function('filter'). 
Therefore, the int function is applied to each element in number_str, 
converting each string to an integer, and the result is then converted to a list.

So, the output will indeed be ['1', '2', '3', '4', '5'], 
as each element is treated as a string and not filtered based on any condition. 
"""
# Wrong script 2 - tried to call different lower order function in one script but mix wrongly
# print(list(result(is_even, list(result(int, number_str)))))
"""
The script have 2 higher order function 'results'
firstly it will run the int filter 
"""
# Wrong script 3
result = call_function("filter")
filtered_result = filter(lambda x: is_even(int(x)), number_str)
print(
    list(filtered_result)
)  # The script did not change the type of the x, so it still output the original string type

print("reduce")
result = call_function("reduce")
print(result(add_two_nums, number_str))

print("Exercise 4".center(80, "-"))
print("Use for loop to print each country in the countries list.")

# Given lists:
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Exercise 4".center(80, "-"))
for country in countries:
    print(country)
print("Exercise 5".center(80, "-"))
for name in names:
    print(name)
print("Exercise 6".center(80, "-"))
for number in numbers:
    print(number)

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
lst_uppercase = map(lambda country: country.upper(), countries)
print(list(lst_uppercase))

print("Exercise 2".center(80, "-"))
lst_square = map(lambda a: a**2, numbers)
print(list(lst_square))

print("Exercise 3".center(80, "-"))
print("Use map to change each name to uppercase in the names list")


def change_uppercase(lst):
    uppercase_lst = []
    for i in lst:
        uppercase_lst.append(i.upper())
    return uppercase_lst


print(list(map(change_to_upper, names)))

print("Exercise 4".center(80, "-"))
print("Use filter to filter out countries containing 'land'.")


def if_include_land(str):
    if "land" in str:
        return True
    else:
        return False


country_include_land = filter(if_include_land, countries)
print(list(country_include_land))

print("Exercise 5".center(80, "-"))
print("Use filter to filter out countries having exactly six characters.")


def len_equal_to_six(str):
    if len(str) == 6:
        return True
    else:
        return False


six_characters_countries = filter(len_equal_to_six, countries)
print(list(six_characters_countries))

print("Exercise 6".center(80, "-"))
print(
    "Use filter to filter out countries containing seven letters and more in the country list."
)


def len_longer_than_6(str):
    if len(str) > 6:
        return True
    else:
        return False


five_more_characters_countries = filter(len_longer_than_6, countries)
print(list(five_more_characters_countries))

print("Exercise 7".center(80, "-"))
print("Use filter to filter out countries starting with an 'E'")


def start_e(str):
    if str[0] == "E":
        return True
    else:
        return False


start_e_country = filter(start_e, countries)
print(list(start_e_country))

print("Exercise 8".center(80, "-"))
print(
    "Chain two or more list iterators \n(eg. arr.map(callback).filter(callback).reduce(callback))"
)
# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chain multiple operations
result = reduce(
    lambda acc, x: acc + x, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers))
)
print(result)
"""
run according to this sequence
map(lambda x: x * 2, numbers) #2,4,6,...,20
filter(lambda x: x % 2 == 0,lst) #All the nunmbers are even
reduce(lambda acc, x: acc + x,lst) #Accumate all list items
#2+4+6+...+20=110
This type of the multiple chain script is not readable.
So prefer to use list comprehensions or plain loops for better readability
"""

print("Exercise 9".center(80, "-"))
print(
    "Declare a function called get_string_lists which takes a list as a parameter \nand then returns a list containing only string items."
)

# lst = [1,3,5,'lx','bodybuilder',(4,7),{4,10}]
# def get_string_lists(lst):
#     for i in lst:
# The mistake is my function tried to iterate through the list before using filter function. Which is not correct filter conditions
#         if type(i) == str:
#             return True
#     return False

# string_list = filter(get_string_lists, lst)
# print(list(string_list))

lst = [1, 3, 5, "lx", "bodybuilder", (4, 7), {4, 10}]


def get_string_lists(i):
    if type(i) == str:
        return True
    return False


# The conditional function only use for single items, not iterate

string_list = filter(get_string_lists, lst)
print(list(string_list))

print("Exercise 10".center(80, "-"))
print("Use reduce to sum all the numbers in the numbers list.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_lst = reduce(lambda a, b: a + b, numbers)
print(sum_lst)

print("Exercise 11".center(80, "-"))
print(
    "Use reduce to concatenate all the countries and to produce this sentence: \nEstonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"
)
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
print("\n")


def sample_sentence(lst):
    complete_sentences = ""
    i = 0
    while i < len(lst):  # 6 total, #0,1,2,3,4
        if i == len(lst) - 2:  # 4
            complete_sentences = complete_sentences + lst[i]
            break
        complete_sentences = complete_sentences + lst[i] + ", "
        i += 1  # 1,2,3,4
    complete_sentences = (
        complete_sentences + " and " + lst[-1] + " are north European countries."
    )
    return complete_sentences


# output = reduce(sample_sentence, countries)
# print(output)

print(sample_sentence(countries))


countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


def concatenate_countries(sentence, country):
    if sentence:  # an empty string is considered falsy, and any non-empty string is considered truthy.
        return (
            sentence + ", " + country
        )  # if the sentence already have the value, then need add ','
    else:
        return country  # If the sentence dont hv value yet, then just start the country


output = reduce(concatenate_countries, countries)

final_sentence = output + " are north European countries."
print(final_sentence)

print("Exercise 12".center(80, "-"))
print(
    "Declare a function called categorize_countries that returns a list of countries with some common pattern you can find the countries list in this repository as countries.js."
)

file_path = "data/countries.py"
with open(file_path, "r") as file:
    script_content = file.read()

exec(script_content)  # Read the file

print("Method 1: List Comprehension Method".center(80, "-"))


def categorize_countries(key_word):
    # country_list_key_word = [country_key_Word for country_key_Word in country for country in countries if key_word in country_key_Word]
    result = [country for country in countries if key_word in country]
    return result


print(categorize_countries("land"))


print("Method 2: ChatGPT Method".center(80, "-"))


def categorize_countries(key_word):
    result = list(filter(lambda country: key_word in country, countries))
    return result


print(categorize_countries("ia"))

print("Exercise 13".center(80, "-"))
print(
    "Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter."
)

print("Method 1 - define a dictionary by self".center(80, "-"))
output_dic = {}
for country in countries:
    if country[0] not in output_dic:
        output_dic[country[0]] = 1
    else:
        output_dic[country[0]] += 1
print(output_dic)

print("Method 2 - define a dictionary through collections defaultdic".center(80, "-"))
from collections import defaultdict

output_dic = defaultdict(int)
for country in countries:
    output_dic[country[0]] += 1

print(output_dic)

# show an example of defaultdict, () can define a type of the value by default
x = defaultdict(int)  # When define the value is the int
print(f"{x['A'] = }")

x["A"] = 5
print(f"{x['A'] = }")

y = defaultdict(list)
print(
    f"{y['A'] = }"
)  # When define the value is the list, the empty key value is the empty list

print("Exercise 14".center(80, "-"))
print(
    "Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder."
)


def get_first_ten_countries():
    countries_first_ten = countries[0:10]
    return countries_first_ten


print(get_first_ten_countries())

print("Exercise 15".center(80, "-"))
print(
    "Declare a get_last_ten_countries function that returns the last ten countries in the countries list."
)


def get_last_ten_countries():
    countries_last_ten = countries[-10:]
    return countries_last_ten


print(get_last_ten_countries())

print("Exercise Level 3".center(80, "-"))
print("Exercise 1".center(80, "-"))
print("Use the countries_data.py file and follow the tasks below:")
print("Sort countries by name, by capital, by population")

file_path = "data/countries_data.py"
with open(file_path, "r", encoding="utf-8") as file:
    script_content = file.read()

exec(script_content)  # Read the file

# Rmr always use sorted to return new list
# Sort multiple key for dictionary
for country in countries:
    sorted_countries = sorted(
        countries_data, key=lambda x: (x["name"], x["capital"], x["population"])
    )

print(countries_data[:3])

print("Exercise 2".center(80, "-"))
print("Sort out the ten most spoken languages by location.")

"""
example output:
English: america, chinese, finland..
chinese: China, finland..
"""

output_country_dic = defaultdict(list)
for country in countries_data:
    for language in country["languages"]:
        # output_country_dic[language] += country['name']
        """
        Mistake 1:
        Cannot use the += in a dictionary
        country['name'] is a string representing the name of the country, 
        and using += with a list and a string will not append the string as an element to the list.
        Mistake 2:
        output_country_dic[language] += list(country['name']) 
        By usinglist() to a string, it will convert to a list of characters
        Not good practice 1:
        output_country_dic[language] += [country['name']] 
        Can work, but not an effective way to convert a string then using extend +=
        """
        output_country_dic[language].append(country["name"])
print(
    output_country_dic
)  # sample output {'Vietnamese': ['Viet Nam'], 'Shona': ['Zimbabwe'], 'Northern Ndebele': ['Zimbabwe']}
# sorted_output_country_dic = sorted(output_country_dic, key = lambda x: len(x.values()), reverse = True)
# Why this cannot work ? AttributeError: 'str' object has no attribute 'values'
print("sorted output country")
sorted_output_country_dic = sorted(
    output_country_dic.items(), key=lambda x: len(x[1]), reverse=True
)
print(sorted_output_country_dic[:10])

print("Chatgpt example")
data = [
    {"name": "JohnN", "numbers": [1, 2, 3]},
    {"name": ["Alice", "a", "b", "c"], "numbers": [4, 5]},
    {"name": ["Bob", "4", "e"], "numbers": [6, 7, 8, 9]},
]
sorted_data = sorted(data, key=lambda x: len(list(x.values())[0]), reverse=True)
# Sort by first value, which is comparing length of 'JohnN' , ['Alice','a','b','c'], ['Bob','4','e']
for item in sorted_data:
    print(item)

print("example from lx")
list_of_dicts = [
    {"a": ["hello"], "b": ["world", "python"]},
    {"x": ["python", "coding", "is", "fun"], "y": ["hello"]},
    {"k": ["openai"], "l": ["gpt"], "m": ["chatgpt", "cool"]},
]

# Sorting the list of dictionaries by the length of the longest list in their values
sorted_list = sorted(list_of_dicts, key=lambda d: max(len(v) for v in d.values()))

print(sorted_list)

print("Exercise 3".center(80, "-"))
print("Sort out the ten most populated countries.")
output_most_populated_country = defaultdict(int)
for country in countries_data:
    output_most_populated_country[country["name"]] = country["population"]

list_populated_country = list(
    output_most_populated_country.items()
)  # Convert the item type to list of tuples
list_populated_country.sort(
    key=lambda x: x[1], reverse=True
)  # Sort by each tuple second value
print(list_populated_country[:10])

# Method 2 -Presentation different
# list_populated_country = list(output_most_populated_country.items())
# print(list_populated_country)
# list_populated_country.sort(key=lambda x: x[1], reverse=True)
# print(f"Top {10} most populated countries in the world: ")
# for country, population in list_populated_country[:10]:
#     print(f"{country}: {population}")
