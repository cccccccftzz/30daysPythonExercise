#Exception Handling

from datetime import datetime

print("Catch up in Preview".center(80, "-"))
try:
    print(5 + '10')
except:
    print('Something went wrong')

try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')

    current_day = datetime.now()
    current_year = current_day.year

    age = 2024 - int(year_born)
    print(f'You are {name}. And you age is {age}')
except:
    print('Something went wrong.')

print(f'To give the exception with the error type defined')
try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')

    current_day = datetime.now()
    current_year = current_day.year

    age = 2024 - int(year_born)
    print(f'You are {name}. And you age is {age}')
except TypeError:
    print('Type Error occured.')
except ValueError:
    print('Value Error occured.')
except ZeroDivisionError:
    print('Zero division Error occured.')
else:
    print('I usually run with the try block.') 
    #As long as no exception occured, Run this code
finally:
    print('I will always run.')
    #Always run this code

try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')

    current_day = datetime.now()
    current_year = current_day.year

    age = 2024 - int(year_born)
    print(f'You are {name}. And you age is {age}')
except Exception as e:
    print(e) 
    #invalid literal for int() with base 10: 'k'
    #base 10 stands for 十进制

print('Packing and Unpacking Arguments in Python'.center(80, "-"))
'''
* for tuples
** for dictionaries
'''
print('Unpacking List'.center(80, "-"))
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

args = [2, 7]
numbers = range(*args) # call with arguments unpacked from a list
print(numbers) #range(2, 7)

print('Unpacking Tuple'.center(80, "-"))
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) 
# Finland Sweden Norway ['Denmark', 'Iceland']
#',' here is just a syntax, will not print out inlcuding ','

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

print('Unpacking Dictionaries'.center(80, "-"))
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. She is {age} year old.'
dct = {'name':'Fang Ting',
       'country' : 'China',
       'city' : 'Shanghai',
       'age' : 18
       }
print(unpacking_person_info(**dct))
#Unpacking dictionaries -> To distribute the dic value to the assigned locations.

print('Packing'.center(80, "-"))
print('Packing List'.center(80, "-"))
def sum_all(*args): #Input a lot numbers but only assign one argument
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3, 4))
print(sum_all(1, 2, 3, 4, 7, 8, 10))

print('Packing Dictionaries'.center(80, "-"))
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')  #When packing, to use "=" instead of ":"
    return kwargs

print(packing_person_info(name = 'Fang Ting', country = 'China', city = 'Shanghai', age = 18))
#Directly packing those info into one dictionary and print it as ONE argument

print('Spreading in Python'.center(80, "-"))
#Spreading is just merge two same types into one extended type
lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
lst = [*lst_one, *lst_two]
print(lst)

print('Enumerate'.center(80, "-"))
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    print('Hi!')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}.')

for index, item in enumerate([20, 30, 40]):
    print(index, item)     
'''
0 20
1 30
2 40
'''

print('Zip'.center(80, "-"))
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegs = []
for f, v in zip(fruits, vegetables): #Use zip function here to packing two members tgt
    fruits_and_vegs.append({'fruit' : f, 'veg' : v}) #As one argument --set
print(fruits_and_vegs)

print('Exercise 1'.center(80, "-"))
'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
Unpack the first five countries and store them 
in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)


