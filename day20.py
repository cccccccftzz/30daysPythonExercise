# PIP

print("Catch up in Preview".center(80, "-"))

#PIP stands for Preferred installer program

#My pip version :pip 23.2.1 

#Installing packages using 'pip <packagename>'
#Uninstalling packages using 'pip uninstall <packagename>'

#To check all installed pip by 'pip list'

#To show information about a package 'pip show <packagename>'

# Package - numpy
# To check the pip module version by' pip show numpy'
import numpy
'''
Name: numpy
Version: 1.26.3
Summary: Fundamental package for array computing in Python
'''
lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst) #To convert a list to an array in python
print(np_arr) #[1 2 3 4 5]
print(len(np_arr)) #5

print(np_arr * 2) #[ 2  4  6  8 10]

print(np_arr + 2) #[3 4 5 6 7]

'''The spacing is not indicative of any specific property or difference in the array's data; 
it's purely for presentation purposes'''

# Package - pandas 
'''
Name: pandas
Version: 2.1.4
Summary: Powerful data structures for data analysis, time series, and statistics
'''

# Web browser module - can open any website 
import webbrowser
url_lists = [
    'http://www.python.org',
    'www.linkedin.com/in/fangting-chen-8a5112125',
    'https://github.com/cccccccftzz',
]

# for url in url_lists:
#     webbrowser.open_new_tab(url) #in any default webbrowser

print("Reading from URL".center(80, "-"))

import requests

print('Read a txt file from the website'.center(80, "-"))
url = 'https://www.gutenberg.org/cache/epub/73081/pg73081.txt' # text from a website
response = requests.get(url)
print(response) #<Response [200]>, 200 means successfully opened
print(response.status_code) #404 fail to open, 200 means successfully opened
print(response.headers) # {'date': 'Sat, 02 Mar 2024 04:36:47 GMT', 'server': 'Apache', 'last-modified': 'Fri, 01 Mar 2024 11:00:46 GMT', 'accept-ranges': 'bytes', 'content-length': '80407', 'x-backend': 'gutenweb1', 'content-type': 'text/plain; charset=utf-8'}
response.text #To read the text in the link, and give a variable

print("Read a API from the website".center(80, "-"))
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])


print("Creating a package".center(80, "-"))
#Created a mypackage in the same folder directory and created two .py files and one init.py file
# The init.py is essential for the folder to be recognized by Python as a package.
#Now the mypackage folder are treated as one package alr

from mypackage import arithmetics, greet

print(arithmetics.add_numbers(1, 2, 3, 4))
print(arithmetics.subtract(1, 4))
print(greet.greet_person('Fangting','Chen')) 
'''
Syntax:
from package import module1, module2
module.function()
'''


print('Exercises Level 1'.center(80, "-"))
print('''Read a url and find the 10 most frequent words.''')
import requests

url = 'https://www.gutenberg.org/cache/epub/73074/pg73074.txt'
response = requests.get(url)
print(f'{response}') #<Response [200]>, 200 means successfully opened
print(f'{response.status_code}') 

main_txt = response.text 
print(type(main_txt)) #string, When get the text alr, it becomes a string type alr

#Method 1 - from package import module
from mypackage import mostcommonword
mostcommonword.find_most_common_words(main_txt, 5)  #module.function()

#Method 2 - from package import module
import mypackage.mostcommonword as mostcommonword
mostcommonword.find_most_common_words(main_txt, 5) #module.function()

#Method 3 - from module import function
from mypackage.mostcommonword import find_most_common_words
find_most_common_words(main_txt, 5) #Direction function()

from mypackage import mostrepeatedword
mostrepeatedword.most_repeated_words(main_txt, 10) 

'''
To take note that when import a certain function from one module,
it also will run through all the rows in the module
if got any output in the module even not inside the function it also will print out
'''

print('Exercises Level 2'.center(80, "-"))
print('''
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
''')

import requests
import statistics
from pprint import pprint

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response.status_code)
print(response.headers.get('Content-Type', '')) #If does not find 'Content-Type', to output ''space instead to handle the error.
contents = response.json()
print(type(contents)) #List, list of dictionaries
'''
The requests library internally handles the JSON parsing, 
and response.json() returns the parsed JSON data as a Python object (usually a dictionary or a list).

'''

#To print out the list of the keys in the subdictionary for later finding the value
for content in contents:
    pprint(content, indent=4)
    print(content.values())
    break

print('a)the min, max, mean, median, standard deviation of cats weight in metric units.')

cat_min_weight_info_lst = [float(weight_boundary) for cat_info in contents for weight_boundary in cat_info['weight']['metric'].split(' - ') ] #To save all the upper and lower bound in the list
#Why sometimes the subitem in front? sometimes the overall item in front?
min_cat_weight = min(cat_min_weight_info_lst)
print(f'{min_cat_weight = } metrics')

cat_max_weight_info_lst = [float(cat_info['weight']['metric'].split()[2]) for cat_info in contents]
max_cat_weight = max(cat_max_weight_info_lst)
print(f'{max_cat_weight = } metrics')

cat_weight_info_lst_mean = [statistics.mean([float(cat_info['weight']['metric'].split()[2]),float(cat_info['weight']['metric'].split()[0])]) for cat_info in contents]
mean_cat_weight = statistics.mean(cat_weight_info_lst_mean)
print(f'{mean_cat_weight = :.2f} metrics')
    
median_cat_weight = statistics.median(cat_weight_info_lst_mean)
print(f'{median_cat_weight = :.2f} metrics')

stdev_cat_weight = statistics.stdev(cat_weight_info_lst_mean)
print(f'{stdev_cat_weight = :.2f} metrics')

print('b) the min, max, mean, median, standard deviation of cats\' lifespan in years.')

cat_min_lifespan_info_lst = [float(lifespan_boundary) for cat_info in contents for lifespan_boundary in cat_info['life_span'].split(' - ') ] 
min_cat_lifespan = min(cat_min_lifespan_info_lst)
print(f'{min_cat_lifespan = } years')

cat_max_lifespan_info_lst = [float(lifespan_boundary) for cat_info in contents for lifespan_boundary in cat_info['life_span'].split(' - ') ] 
max_cat_lifespan = max(cat_min_lifespan_info_lst)
print(f'{max_cat_lifespan = } years')

cat_mean_lifespan_info_lst = [statistics.mean([float(cat_info['life_span'].split(' - ')[1]),float(cat_info['life_span'].split(' - ')[0])]) for cat_info in contents] 
mean_cat_lifespan = statistics.mean(cat_mean_lifespan_info_lst)
print(f'{mean_cat_lifespan = :.2f} years')

cat_median_lifespan_info_lst = [statistics.mean([float(cat_info['life_span'].split(' - ')[1]),float(cat_info['life_span'].split(' - ')[0])]) for cat_info in contents] 
median_cat_lifespan = statistics.median(cat_median_lifespan_info_lst)
print(f'{median_cat_lifespan = :.2f} years')

cat_median_lifespan_info_lst = [statistics.mean([float(cat_info['life_span'].split(' - ')[1]),float(cat_info['life_span'].split(' - ')[0])]) for cat_info in contents] 
stdev_cat_lifespan = statistics.stdev(cat_median_lifespan_info_lst)
print(f'{stdev_cat_lifespan = :.2f} years')

print('c) Create a frequency table of country and breed of cats ')
# breed of cats 'name'
#  country 'origin'

from collections import defaultdict, Counter

country_breed_dic = defaultdict(list)
for cat_info in contents:
    country_breed_dic[cat_info['origin']].append(cat_info['name'])

print(country_breed_dic)

country_breed_count = {country: len(breeds) for country, breeds in country_breed_dic.items()}
print(country_breed_count)
print(f'Frequency table of Country & Bread of cats:')
print(f'{'Country':^20} {'Count':^5} List of Country')
for country, count in country_breed_count.items():
    print(f'{country:^20}{count:^5}{country_breed_dic[country]}')

#Exercise 3 skipped due to the link expired.

#Exercise 4 will be self learning