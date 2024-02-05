# Strings

print("Catch up in Preview".center(80, "-"))
first_name = "Fang Ting"
last_name = "Chen"
space = " "
full_name = first_name + space + last_name
print(last_name + "\n" + full_name)
print(len(full_name))

# Practice for \n, \t, \\, \', \"
print('Practice for "\\n", \\t, \\\, \\\', \\"'.center(80, "-"))

print("I hope everyone is enjoying the Python challenge. \nAre you?")
print("Days\tTopic\tExercises")
print("Day 1\t5\t5")
print(
    "This is a backlash sybom (\\)"
)  # If only write one \ cannot print, need write double \\
print('In every programming language it starts with "Hello, World!"')

# Old school formatting:Practice for %s, %d, %f, %.number of digitsf
print("Practice for %s, %d, %f, %.number of digitsf".center(80, "-"))

# Strings only
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am %s %s. I teach %s" % (first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of the circle with a radius %d is %.2f." % (radius, area)
print(formated_string)

# New Style formatting 1 ".format()"
print('New Style Formatting 1 ".format ()"'.center(80, "-"))

first_name = "Fang Ting"
last_name = "Chen"
language = "Chinese"
formated_string = "I am {} {}. I teach {}".format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3
print(" {} + {} = {} ".format(a, b, a + b))  # "()" always to be the outest
print(" {} - {} = {} ".format(a, b, a - b))
print(" {} * {} = {} ".format(a, b, a * b))
print(" {} / {} = {:.2f} ".format(a, b, a / b))
print(" {} % {} = {} ".format(a, b, a % b))
print(" {} // {} = {} ".format(a, b, a // b))
print(" {} ** {} = {} ".format(a, b, a**b))

formated_string = "The area of the circle with a radius {} is {:.2f}.".format(
    radius, area
)
print(formated_string)

# New Style formatting 2 f-string f''
print("New Style formatting 2 f-string f''".center(80, "-"))

print(f" {a} + {b} = {a+b} ")
print(f" {a} - {b} = {a-b} ")
print(f" {a} * {b} = {a*b} ")
print(f" {a} / {b} = {a/b:.2f} ")
print(f" {a} % {b} = {a%b} ")
print(f" {a} // {b} = {a//b} ")
print(f" {a} ** {b} = {a**b} ")

# Strings as sequences of charactors
print("Strings as sequences of charactors".center(80, "-"))

language = "Python"
a, b, c, d, e, f = language
print("Every letter in Python: ")
print(len(language))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


print("First letter, second letter and last letter of Python: ")
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_letter_index = len(language) - 1
last_letter = language[last_letter_index]
print(last_letter)

print("Last letter and second last letter of Python: ")
last_letter = language[-1]
print(last_letter)
second_letter = language[-2]
print(second_letter)

print("First 3 letters and last 3 letter of Python: ")
first_three_letter = language[0:3]
print(first_three_letter)
first_three_letter = language[:3]
print(first_three_letter)
last_three_letter = language[3:6]  # 3,4,5
print(last_three_letter)
last_three_letter = language[-3:]  # -3,-2,-1
print(last_three_letter)
last_three_letter = language[3:]  # 3,4,5
print(last_three_letter)

# Reversing Strings
print("Reversing Strings".center(80, "-"))
greeting = "Hello, World!"
print(greeting[::-1])
"""
"::" means that it will consider the entire string
the negative step '-1 indicates that the slicing should be done in reverse
"""
print(greeting[::])  # "::" means that it will consider the entire string

# Skipping Strings
print("Skipping Strings".center(80, "-"))
language = "Python"
print(language)
pto = language[0:6:2]  # 0~5 but step is 2, meaning to print 0,2,4
print(pto)

# Strings Methods
print("Strings Methods".center(80, "-"))
challenge = "thirty days of python"
print(challenge.count("y", 7, 14))

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
challenge = ["thirty days of python"]
print(
    challenge.count("of")
)  # when checking the list with one argument only, cannot specify the location

# capitalize(): Converts the first character of the string to capital letter
challenge = "thirty days of python"
print(challenge.capitalize())  # Only can capitalize STRINGS type!!

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith("ython"))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = "thirty\tdays\tof\tpython"
print(
    challenge.expandtabs()
)  # Replaces tab character with spaces, default tab size is 8
print(challenge.expandtabs(10))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = "thirty days of python"
print(challenge.find("y", 7, 14))
print(challenge.find("y"))
print(challenge.find("th"))  # start from first substring, which is the first one "0"
print(challenge.find("hi"))
print(challenge.find("c"))  # returns -1 meaning cannot find any

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = "thirty days of python"
print(challenge.rfind("y"))  # find the index of last occurrence of substring
print(challenge.rfind("th"))  # to give 't' index which is 17

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
sub_string = "da"
print(challenge.index(sub_string))  # To return the index of "d", 7
print(
    challenge.index(sub_string, 0, 12)
)  # If cannot find any between (0,12), it will return error

# rindex(): finds the last occurrence of the specified value, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "y"
print(challenge.rindex(sub_string))  # finds the last occurrence of the specified value.
sub_string = "da"
# print (challenge.rindex(sub_string,0,8)) #error. "a" index is 8, but the substring is not completely included in the specified length, so cannot find still
print(challenge.rindex(sub_string, 0, 9))  # 7

# isalnum(): Checks alphanumeric character
challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True
challenge = "30DaysPython"
print(challenge.isalnum())  # True
challenge = "thirty days of python"
print(challenge.isalnum())  # False, space is not an alphanumeric character
challenge = "thirty days of python 2019"
print(challenge.isalnum())  # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = "thirty days of python"
print(challenge.isalpha())  # False, space is once again excluded
challenge = "ThirtyDaysPython"
print(challenge.isalpha())  # True
num = "123"
print(num.isalpha())  # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = "thirty days of python"
print(challenge.isdecimal())  # False
challenge = "123"
print(challenge.isdecimal())  # True
challenge = "123.68"
print(challenge.isdecimal())  # False
challenge = "\u00B2"
print(challenge.isdecimal())  # False
challenge = "12 3"
print(challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = "Thirty"
print(challenge.isdigit())  # False
challenge = "30"
print(challenge.isdigit())  # True
challenge = "\u00B2"
print(challenge.isdigit())  # True ??? what is this

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = "10"
print(num.isnumeric())  # True
num = "\u00BD"  # ½
print(num.isnumeric())  # True ??? what is this
num = "10.5"
print(num.isnumeric())  # False

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = "30DaysOfPython"
print(challenge.isidentifier())  # False, because it starts with a number
challenge = "thirty_days_of_python"
print(challenge.isidentifier())  # True

# islower(): Checks if all alphabet characters (CAN HV numeric) in the string are lowercase
challenge = "30DaysOfPython"
print(challenge.islower())  # false
challenge = "30daysofpython"
print(challenge.islower())  # True

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = "thirty days of python"
print(challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True

# join(): Returns a concatenated string
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " ".join(web_tech)  # Inserting a space when joining the list member
print(result)
web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = "#".join(web_tech)
print(result)

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = "thirty days of pythooonnn"
print(challenge.strip("noth"))  # 'irty days of py'

# replace(): Replaces substring with a given string
challenge = "thirty days of python"
print(challenge.replace("python", "coding"))  # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator
challenge = "thirty days of python"
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = "thirty, days, of, python"
print(challenge.split(", "))  # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
challenge = "thirty days of python"
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = "thirty days of python"
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = "thirty days of python"
print(challenge.startswith("thirty"))  # True
challenge = "30 days of python"
print(challenge.startswith("30 "))  # True

print("Exercise 1".center(80, "-"))
string_exercise_one = ["Thrity", "Days", "of", "Python"]
result_exercise_one = " ".join(string_exercise_one)
print(result_exercise_one)

print("Exercise 2".center(80, "-"))
string_exercise_two = ["Coding", "for", "All"]
result_exercise_two = " ".join(string_exercise_two)
print(result_exercise_two)

print("Exercise 3-8".center(80, "-"))
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print("Exercise 9".center(80, "-"))
# Cut(slice) out the first word of Coding For All string.
abc = "Codings for all"
after_slice = abc.split()[1:]
join_after_slice = " ".join(after_slice)
print(join_after_slice)

# How to print the Codings
print(abc.split())  # list of str
coding = abc.split()[0]
print(coding)
print(abc[0:8])  # " " index is 7, so print enb until 8
print(abc[8:])  # "f" index is 8, so print start from 8

print("Exercise 10".center(80, "-"))
# Check if Coding For All string contains a word Coding using the method index, find or other methods.

# Method 1 - using find ()
print("Method 1 - using find ()".center(40, "~"))
abc = "Codings for all"
whether_have_codings = abc.find("Codings")
print(
    f'{"Cannot find" if whether_have_codings == -1 else "Can find" } \'Codings\' in the strings'
)

# Method 2 case 1 - Typical mistakes by using index ()
print("Method 2 case 1 - Typical mistakes by using index ()".center(70, "~"))
abc = "Codings for all"
whether_have_for = abc.index("for")
print(
    f'{"Cannot find" if whether_have_codings != -1 else "Can find" } \'for\' in the strings'
)
# To take note if cannot find, it won't == -1, it will return error

# Method 2 case 2 - using index () when cannot find return errors
print("Method 2 case 2 - using index () when cannot find return errors".center(70, "~"))
sentence = "Codin For All"
try:
    index = sentence.index("Coding")
    print("The substring 'Coding' is present at index:", index)
except ValueError as e:
    print("The substring 'Coding' is not found in the string.")


print("Exercise 11".center(80, "-"))
# Replace the word coding in the string 'Coding For All' to Python.
abc = "Codings For All"
print(abc.replace("Codings", "Python"))

print("Exercise 12".center(80, "-"))
# Change Python for Everyone to Python for All using the replace method or other methods.
abc = "Python for Everyone"
print(abc.replace("Everyone", "All"))

print("Exercise 13".center(80, "-"))
# Split the string 'Coding For All' using space as the separator split())
abc = "Python for Everyone"
print(abc.split())

print("Exercise 14".center(80, "-"))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
abc = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(abc.split(","))

print("Exercise 15~17".center(80, "-"))
# What is the character at index 0 in the string Coding For All.
abc = "Coding For All"
print(abc[0])

# What is the last index of the string Coding For All.
print(len(abc) - 1)

# What character is at index 10 in "Coding For All" string.
print(abc[10])

print("Exercise 18".center(80, "-"))
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("Method 1 - My own method".center(40, "~"))
abc = "python for everyone"
split_abc = abc.split()
print(split_abc)
acronym = ""
for word in split_abc:
    acronym += word[0]
print(acronym.upper())

print("Method 2".center(40, "~"))
# Define the phrase
phrase = "Python For Everyone"
# Create an acronym
acronym = "".join(word[0].upper() for word in phrase.split())
# Don't understand why for loop to be returned everytime when using join function.
# Print the result
print(acronym)

print("Exercise 19".center(80, "-"))
# Use index to determine the position of the first occurrence of C in Coding For All.
phrase = "Coding for All"
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)

print("Exercise 20~21".center(80, "-"))
# Use index to determine the position of the first occurrence of C in Coding For All.
abc = "Coding for All"
print(abc.index("C"))
print(abc.index("f"))
print(abc.rfind("l"))
print(abc.rindex("l"))

print("Exercise 22".center(80, "-"))
# se rfind to determine the position of the last occurrence of l in Coding For All People.
abc = "Coding for All People"
print(abc.rindex("P"))  # capital different

print("Exercise 23~24".center(80, "-"))
# Use index or find to find the position of the first & last occurrence of the word 'because'
abc = "You cannot end a sentence with because because because is a conjunction"
print(abc.index("because"))  # The first accurrence
print(abc.rindex("because"))  # The last accurrence

print("Exercise 25".center(80, "-"))
# Slice out the phrase 'because because because'
abc = "You cannot end a sentence with because because because is a conjunction"
location_of_start = abc.index("because because because ")
location_of_end = (
    location_of_start + len("because because because ") - 1
)  # rmr to minus 1 when using len()
abc_part_one = abc[:location_of_start]
abc_part_two = abc[(location_of_end + 1) :]
print(abc_part_one + abc_part_two)
print(abc[location_of_start : location_of_start + len("because because because")])

print("Exercise 28~29".center(80, "-"))
# Does ''Coding For All' start with a substring Coding?
abc = "Coding For All"
print(abc.startswith("Coding"))
print(abc.endswith("Coding"))

print("Exercise 30".center(80, "-"))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
abc = "   Coding For All      "
print(abc.strip(" "))

print("Exercise 31".center(80, "-"))
abc = "30DaysOfPython"
print(abc.isidentifier())
abc = "thirty_days_of_python"
print(abc.isidentifier())

print("Exercise 32".center(80, "-"))
lst = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(lst))

print("Exercise 33".center(80, "-"))
# Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge. \nI just wonder what is next.")

print("Exercise 34".center(80, "-"))
# Use a tab escape sequence to write the following lines.
tab_list = "Name\tAge\tCountry\tCity"
tab_list_one = "Asabeneh\t250\tFinland\tHelsinki"
print(tab_list.expandtabs(12))
print(tab_list_one.expandtabs(12))

print("Exercise 35".center(80, "-"))
# Use the string formatting method to display the following:
radius = 10
area_of_circle = 3.14 * (radius**2)
print(f"{radius} = ")
print(f"{radius = }")  # To take note the difference!!
print(f"{area_of_circle = }")
print(f"The area of circle of a circle with {radius =} is {area_of_circle:.2f}")

print("Exercise 36".center(80, "-"))
# Make the following using string formatting methods:
a = 8
b = 6
print(f"{a + b = }")
print(f"{a - b = }")
print(f"{a * b = }")
print(f"{a / b = :.2f}")
print(
    f"{a / b = }:.2f"
)  # Wrong location for the formatting, must be followed by the position of the output
print(f"{a % b = }")  # 2
print(f"{a // b = }")  # 1
print(f"{a ** b = }")
