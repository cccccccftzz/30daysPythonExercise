# Function

print("Catch up in Preview".center(80, "-"))
print("default value and arbitrary number of arguments")


# Method 1: print the function while return value still None
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups("Team-1", "Asabeneh", "Brook", "David", "Eyob"))
# To take note there is a 'None' value when running the function done.

# Method 2: Directly run the function and no need print return value
generate_groups("Team-1", "Asabeneh", "Brook", "David", "Eyob")

print("You can pass functions around as parameters")


def cube_number(n):
    return n**n


def do_something(f, x):
    return f(x)


print(do_something(cube_number, 3))  # 27

print("Exercise Level 1".center(80, "-"))
print("Exercise 1".center(80, "-"))
print(
    "Declare a function add_two_numbers. It takes two parameters and it returns a sum."
)


def sum(a, b):
    sum_of_ab = a + b
    return sum_of_ab


print(f"{sum (5,6)}")

print("Exercise 2".center(80, "-"))
print(
    "Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle."
)
import math


def area_of_circle(radius):
    area = math.pi * radius * radius
    return area


print(f"{area_of_circle(1):.2f}")  # Need keep the :.2f format with the variable

print("Exercise 3".center(80, "-"))
print(
    "Write a function called add_all_nums \nwhich takes arbitrary number of arguments and sums all the arguments. \nCheck if all the list items are number types. \nIf not do give a reasonable feedback."
)
# def add_all_nums (*nums):
#     for num in nums:
#         total = 0
#         if (num.isdecimal()):
#             total += num
#         else:
#             print(f'To check the input are decimal format!')
#     return total

# print ( add_all_nums (1,2,3,4,5))


def add_all_nums(*args):
    total = 0

    for num in args:
        if isinstance(
            num, (int, float)
        ):  # isinstance to check the object are certain format.
            # isinstance(object, classinfo) : a checking object, certain format type
            total += num
        else:
            print(f"Warning: Skipping non-numeric value: {num}")

    return total


# Example usage:
result = add_all_nums(1, 2, 3, 4, "3h")
print(f"Sum of numbers: {result}")

print("Exercise 4".center(80, "-"))
print(
    "Temperature in °C can be converted to °F using this formula: \n°F = (°C x 9/5) + 32. \nWrite a function which converts °C to °F, \nconvert_celsius_to-fahrenheit."
)


def convert_celsius_to_fahrenheit(temperature_in_C):
    temperature_in_F = (temperature_in_C * 9 / 5) + 32
    return temperature_in_F


result_temperature = convert_celsius_to_fahrenheit(5)
print(result_temperature)

print("Exercise 5".center(80, "-"))
print(
    "Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer."
)


def check_season(season_for_checking):
    captialize_season_for_checking = season_for_checking.capitalize()
    autumn = {"September", "October", "November"}
    winter = {"December", "January", "February"}
    spring = {"March", "April", "May"}
    summer = {"June", "July", "August"}
    if captialize_season_for_checking in autumn:
        season = "autumn"
    elif captialize_season_for_checking in winter:
        season = "winter"
    elif captialize_season_for_checking in spring:
        season = "spring"
    elif captialize_season_for_checking in summer:
        season = "summer"
    else:
        season = "input wrong!"
    return season


result = check_season("Jan")
print(f" The checking result for the season : {result}")

print("Exercise 6".center(80, "-"))
print(
    "Write a function called calculate_slope \nwhich return the slope of a linear equation"
)


def calculate_slope(x1, x2, y1, y2):
    if x1 == x2:
        raise ValueError("The x coordinates for the two points should be different!")
        # Raise + error exception warning to give the warning to user
    slope = (y2 - y1) / (x2 - x1)
    return slope


result = calculate_slope(3, 5, 6, 7)
print(result)

print("Exercise 7".center(80, "-"))
print(
    "Quadratic equation is calculated as follows: \nax² + bx + c = 0. Write a function \nwhich calculates solution set of a quadratic equation, solve_quadratic_eqn."
)


# Solution: x = (-b ± √ (b2 - 4ac) )/2a
def solve_quadratic_eqn(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c) ** 0.5) / 2 / a
    x2 = (-b - (b**2 - 4 * a * c) ** 0.5) / 2 / a
    return (round(x1, 2), round(x2, 2))


result_quadratic_equ = solve_quadratic_eqn(3, 5, 2)
print(result_quadratic_equ)

print("Exercise 8".center(80, "-"))
print(
    "Declare a function named print_list. \nIt takes a list as a parameter \nand it prints out each element of the list."
)


def print_list(lst_to_print):
    for i in lst_to_print:
        print(i)


result = print_list([1, 4, 7, 5, 343])
print(result)

print("Exercise 9".center(80, "-"))
print(
    "Declare a function named reverse_list. \nIt takes an array as a parameter \nand it returns the reverse of the array (use loops)."
)


def reverse_list(a):
    reversed_list = []
    for member in reversed(a):
        reversed_list.append(member)
    return reversed_list


print(reverse_list(["Monday", "Tuesday", "Wednesday"]))

print("Exercise 10".center(80, "-"))
print(
    "Declare a function named capitalize_list_items. \nIt takes a list as a parameter \nand it returns a capitalized list of items"
)


def capitalize_list_items(a):
    capitalized_list = []
    for i in a:
        capitalized_list.append(i.capitalize())
    return capitalized_list


result = capitalize_list_items(["jerry", "tom", "friend"])
print(result)

print("Exercise 11".center(80, "-"))
print(
    "Declare a function named add_item. \nIt takes a list and an item parameters. \nIt returns a list with the item added at the end."
)


def add_item(a, b):
    if isinstance(a, list):  # isinstance to check the object are certain format.
        # complete_list_a_b = a.append(b) .append() is modifying the list in the original list!!!
        a.append(b)
    else:
        a = "input wrong!"
    return a


result = add_item([1, 2, 3, 4, 5], 7)
print(result)
result = add_item(6, 7)
print(result)
food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))

print("Exercise 12".center(80, "-"))
print(
    "Declare a function named remove_item. \nIt takes a list and an item parameters. \nIt returns a list with the item removed from it."
)


def remove_item(lst, b):
    if isinstance(lst, list):
        if b in lst:
            lst.remove(b)
            result = lst
        else:
            result = "The item is not in the list!"
    else:
        result = "Input wrong!"
    return result


# Test 1
food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "Mango"))

# Test 2
food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "banana"))

# Test 3
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

print("Exercise 13".center(80, "-"))
print(
    "Declare a function named sum_of_numbers. \nIt takes a number parameter \nand it adds all the numbers in that range."
)


def sum_of_numbers(number_for_range):
    sum_result = 0
    for i in range(number_for_range + 1):
        sum_result += i
    return sum_result


print(sum_of_numbers(5))
print(sum_of_numbers(10))

print("Exercise 14".center(80, "-"))
print(
    "Declare a function named sum_of_odds. \nIt takes a number parameter \nand it adds all the odd numbers in that range."
)


def sum_of_odd_numbers(number_for_range_odd):
    sum_result = 0
    for i in range(number_for_range_odd + 1):
        if i % 2 == 0:
            continue
        sum_result += i
    return sum_result


print(sum_of_odd_numbers(5))  # 1+3+5 = 9
print(sum_of_odd_numbers(10))

print("Exercise 15".center(80, "-"))
print(
    "Declare a function named sum_of_even. \nIt takes a number parameter \nand it adds all the even numbers in that - range."
)


def sum_of_even_numbers(number_for_range_even):
    sum_result = 0
    for i in range(number_for_range_even + 1):
        if i % 2 != 0:
            continue
        sum_result += i
    return sum_result


print(sum_of_even_numbers(5))  # 2+4 = 6
print(sum_of_even_numbers(10))  # 2+4+6+8+10=30

print("Exercise: Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
print(
    "Declare a function named evens_and_odds. \nIt takes a positive integer as parameter \nand it counts number of evens and odds in the number."
)


def evens_and_odds(num):
    count_for_even = 0
    count_for_odd = 0
    if num > 0 and isinstance(num, int):
        for i in range(num + 1):  # Including 0, even count starts from 0
            if i % 2 == 0:
                count_for_even += 1
                continue
            count_for_odd += 1
        print(f"The number of odds are {count_for_odd}.")
        print(f"The number of evens are {count_for_even}.")
        # Can also print the result inside the function, rather give or not give return value    else:
    else:
        raise ValueError("To key in a positive integer!")
    return (count_for_even, count_for_odd)


print(evens_and_odds(100))

print("Exercise 2".center(80, "-"))
print(
    "Call your function factorial, \nit takes a whole number 整数 as a parameter \nand it return a factorial of the number"
)


# Presentation 1: To use tuple to show the pair factorial
def factorial(num):
    factorial_list = []
    for i in range(1, num + 1):  # Cannot include 0!!
        a = num / i
        if num % i == 0:  # % is to get the reminaer, // to get the floor division
            factorial_list.append((i, int(a)))
    print(factorial_list)
    return factorial_list


factorial(9)


# Presentation 2: To use the set properties to show the factorial (No repeated)
def factorial(num):
    factorial_list = set()  # How to create an empty set!! But actually set is {}
    for i in range(1, num + 1):  # Cannot include 0!!
        if num % i == 0:  # % is to get the reminaer, // to get the floor division
            factorial_list.add(i)
    print(factorial_list)
    return factorial_list


# print (factorial(9))
factorial(
    9
)  # if only call the function, it also will print the result since it was included in the function

print("Exercise 3".center(80, "-"))
print(
    "Call your function is_empty, \nit takes a parameter and it checks if it is empty or not."
)
""" 
Empty meaning any one of the type
String, list, tuple, dict, set
"""


def is_empty(value):
    if value is None:
        return True
    elif isinstance(value, str) and value.strip() == "":
        return True
    elif isinstance(value, (list, set, tuple, dict)) and not value:
        print(not value)
        """     
        If value is empty, then 'value' itselves means False
        Then 'not value' not value means True
        So not value returns True and it is one of the types mentioned
        """
        return True
    else:
        return False


print(is_empty([]))
print(is_empty("      "))

print("Exercise 4".center(80, "-"))
print(
    "Write different functions which take lists. \nThey should calculate_mean, calculate_median, \ncalculate_mode, calculate_range, calculate_variance, \ncalculate_std (standard deviation)."
)


# Calculate_mean
def calculate_mean(lst):
    sum = 0
    if not lst:
        raise ValueError("The lst cannot be empty")
    elif isinstance(lst, list):
        raise ValueError("The input should be a list type")
    else:
        for i in lst:
            sum += i
        count_lst = len(lst)
        mean_of_lst = sum / len
    return mean_of_lst


# Calculate_median
def calculate_median(lst):
    sum = 0
    if not lst:
        raise ValueError("The lst cannot be empty")
    elif isinstance(lst, list):
        raise ValueError("The input should be a list type")
    else:
        count_lst = len(lst)
        sorted_lst = sorted(lst)
        if count_lst % 2 != 0:  # 5/2=3
            median_index = (count_lst - 1) / 2
            median = sorted_lst[median_index]  # (5-1)/2=2
        else:  # 6/2=3
            median_index_left = count_lst / 2
            average_median = (
                sorted_lst[median_index_left - 1] + sorted_lst[median_index_left]
            ) / 2
            median = average_median
    return median


# Calculate_mode
def calculate_mode(lst):
    sum = 0
    # print(not lst)
    if not lst:  # To confirm lst is empty, not lst = reverse false = true
        raise ValueError("The lst cannot be empty")
    elif not isinstance(
        lst, list
    ):  # To check whether it is not a lst, not True = false
        raise ValueError("The input should be a list type")
    else:
        set_lst = set(lst)
        mode_count = {}
        # Wanna assign a dictionary, key is the number, value is the apperance times
        for i in set_lst:
            mode_count[i] = lst.count(i)
            list_mode_count = list(mode_count.items())
            list_mode_count.sort(key=lambda x: x[1], reverse=True)
        print(f"The mode is {list_mode_count[0][0]}")


calculate_mode([1, 2, 6, 7, 8, 9, 3, 23453, 6, 1, 6, 1, 6, 7])

print("Exercise Level 3".center(80, "-"))
print("Exercise 1".center(80, "-"))
print("Write a function called is_prime, which checks if a number is prime.")


def is_prime(num):
    if not isinstance(num, int):
        raise ValueError("To input a interger!")
    elif num == 1:
        raise ValueError("To input a interger bigger than 1!")
    elif num <= 0:
        raise ValueError("To input a positive interger!")
    else:
        factorial_set = set()
        for i in range(1, num + 1):
            if num % i == 0:
                factorial_set.add(i)
        if len(factorial_set) > 2:
            print(f"The number {num} is not prime.")
        else:
            print(f"The number {num} is prime.")


# is_prime(-1)
# is_prime(1)
is_prime(2)
is_prime(5)
is_prime(9)

print("Exercise 2".center(80, "-"))
print("Write a functions which checks if all items are unique in the list.")


def is_unique(lst):
    if not lst:  # To confirm lst is empty, not lst = reverse false = true
        raise ValueError("The lst cannot be empty")
    elif not isinstance(
        lst, list
    ):  # To check whether it is not a lst, not True = false
        raise ValueError("The input should be a list type")
    else:
        set_lst = set(lst)
        if len(set_lst) == len(lst):
            print("All the items are unique in the list.")
        else:
            print("The items are not unique in the list.")


is_unique([4, 6, 8, 12, 2])
is_unique([12, 6, 8, 12, 2])

print("Exercise 3".center(80, "-"))
print(
    "Write a function which checks \nif all the items of the list are of the same data type."
)


def check_type(lst):
    if not lst:  # To confirm lst is empty, not lst = reverse false = true
        raise ValueError("The lst cannot be empty")
    elif not isinstance(
        lst, list
    ):  # To check whether it is not a lst, not True = false
        raise ValueError("The input should be a list type")
    else:
        count_type = set()
        for i in range(len(lst)):  # length = 6, range(6) including 1,2,3,4,5
            count_type.add(type(lst[i]))
            # print (type(lst[i]))
        # print (count_type)
        if (
            len(count_type) == 1
        ):  # Rmr to check the len! not the count_type value itself
            print("All the items of the list are the same data type")
        else:
            print("All the items of the list are not the same data type")


check_type([(4, 7), 6, 8, 12, 2])
check_type([4, 6, 8, 12, 2])

print("Exercise 4".center(80, "-"))
print("Write a function which check \nif provided variable is a valid python variable")


def check_variable_valid(string_input):
    if string_input[0] in {"-", "e", "@", "$", "%"}:
        print("The variable is not valid!")
    elif string_input[0].isdecimal():  # Dont forget to add () after .isdecimal
        print("The variable is not valid!")
    elif string_input in {"if", "while", "for"}:
        print("The variable is not valid!")
    else:
        print("The variable is valid.")


check_variable_valid("if")
check_variable_valid("3fie")
check_variable_valid("@fie")
check_variable_valid("%jijfie")
check_variable_valid("ijfie")

print("Exercise 5".center(80, "-"))
print(
    "Go to the data folder and access the countries-data.py file. \nCreate a function called the most_spoken_languages in the world. \nIt should return 10 or 20 most spoken languages in the world in descending order. \nCreate a function called the most_populated_countries. \nIt should return 10 or 20 most populated countries in descending order."
)
file_path = "data/countries_data.py"
with open(file_path, "r", encoding="utf-8") as file:
    script_content = file.read()

exec(script_content)  # Execute the script content


def most_spoken_languages(i):
    total_number_of_languages = 0
    list_of_language = []
    for each_country in countries_data:
        list_of_language += each_country["languages"]

    # Find the ten most spoken languages from the data
    set_of_language = set(list_of_language)
    language_counts = {}
    for language in set_of_language:
        language_counts[language] = list_of_language.count(language)
        # To create the pairing dictionary directly -> language:counts

    list_appearance_time_language = list(language_counts.items())
    list_appearance_time_language.sort(key=lambda x: x[1], reverse=True)
    # To sort by the second element in the tuple, and descending

    print(f"Top {i} most spoken languages:")
    for language, count in list_appearance_time_language[:i]:
        print(f"{language}: {count}")
        # For the printing function under for loop.
        # every iteration will be given a new line.


def most_populated_countries(i):
    # Find the 10 most populated countries in the world
    country_population = {}  # Dont forget to create a empty dictionary
    for each_country in countries_data:
        country_population[each_country["name"]] = each_country["population"]

    sort_by_value = lambda x: x[1]
    list_populated_country = list(country_population.items())
    list_populated_country.sort(key=lambda x: x[1], reverse=True)

    print(f"Top {i} most populated countries in the world: ")
    for country, population in list_populated_country[:i]:
        print(f"{country}: {population}")


most_spoken_languages(10)
most_populated_countries(20)
