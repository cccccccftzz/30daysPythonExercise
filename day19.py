#File Handling

print("Catch up in Preview".center(80, "-"))
#File Handling by using open() function
f = open('reading_file_example.txt') # mode(r, a, w, x, t,b)  could be to read, write, update
print(f)

#To read the whole file
txt = f.read()
print(type(txt))

print(txt)
f.close()

#read(XX): To read the limited characters
f = open('reading_file_example.txt') 
txt = f.read(10)
print(txt)
f.close()

#readline(): To only read the first line
f = open('reading_file_example.txt') 
line = f.readline()
print(line)
f.close()

#readlines(): To only read the whole txt LINE BY LINE
f = open('reading_file_example.txt') 
lines = f.readlines()
print(lines)
f.close() #['This is a sample file to try open a file\n', 'the second line of the file\n', '\n']

#splitlines() to get all the linkes as a list
f = open('reading_file_example.txt') 
lines = f.read().splitlines()
print(type(lines)) #List
print(lines) #['This is a sample file to try open a file', 'the second line of the file', '']
f.close()

#Another way to open and close the file: with XXXXX as f:
with open('reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines)) #List
    print(lines) #['This is a sample file to try open a file', 'the second line of the file', '']

#Open file for writing and updating
with open('reading_file_example.txt', 'a') as f: #'a' means append， if the file does not exist it creates a new file
    f.write('This text has to be appended at the end.')

with open('reading_file_example_2.txt', 'w') as f: #'w' means write， if the file does not exist it creates a new file
    f.write('This text has to be appended at the end.')

#Deleting files by using os.remove
import os
os.remove('reading_file_example_2.txt')

#To use condition to print out the case if the file does not exist
if os.path.exists('reading_file_example_3.txt'):
    os.remove('reading_file_example_3.txt')
else:
    print('The file does not exist')

# Different File types
print('File with json Extension (Javascript object or Python dictionary'.center(80, "-"))
# json may use for printing the dictionary 

#Python normal dictionary 
person_dct = {
    'name' : 'Fang Ting',
    'country' : 'Singapore',
    'city' : 'Singapore',
    'skills' : ['Bodybuilding', 'programming', 'design']
}

# JSON: A string form a dictionary
person_json = '''{
    'name' : 'Fang Ting',
    'country' : 'Singapore',
    'city' : 'Singapore',
    'skills' : ['Bodybuilding', 'programming', 'design']
}'''

print('Changing JSON to dictionary'.center(80, "-"))
import json

person_json = '''{
    "name" : "Fang Ting",
    "country" : "Singapore",
    "city" : "Singapore",
    "skills" : ["Bodybuilding", "programming", "design"]
}''' #Create json string format
#Must use "" not ' ' for json module strings

person_dct = json.loads(person_json)# use json.loads() to Change JSON to dictionary
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

print('Change dictionary to JSON'.center(80, "-"))
import json
person = {
    'name' : 'Fang Ting',
    'country' : 'Singapore',
    'city' : 'Singapore',
    'skills' : ['Bodybuilding', 'programming', 'design']
} #python dictionary

person_json = json.dumps(person, indent = 4) #indent could be 2, 4, 8. 
#using json.dumps() to change dictionaryto JSON
print(type(person_json))
print(person_json)

print(f'saving as JSON file'.center(80, "-"))
person = {
    'name' : 'Fang Ting',
    'country' : 'Singapore',
    'city' : 'Shanghai',
    'skills' : ['Bodybuilding', 'programming', 'design']
} #python dictionary
with open('writing_json_example', 'w', encoding = 'utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent = 4)

''' encoding='utf-8' parameter specifies that the file should be opened with UTF-8 encoding. 
UTF-8 is a widely used character encoding that can represent most of the characters in the Unicode character set
'''

print('file with csv Entension'.center(80, "-"))
#csb used to store tabular data i.e. spreadsheet or database
import csv
with open ('csv_sample.csv') as f:
    csv_reader = csv.reader(f, delimiter = ',') #csv.reader is same as 'w' use
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {",".join(row)}')
            line_count += 1
        else: 
            print(
                f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.'
            )    
            line_count += 1
        print(f'Number of lines: {line_count}')

print('file with xlsx Entension'.center(80, "-"))
# import xlrd # To read the excel files we need to install xlrd package
# excel_book = xlrd.open_workbook('ST21_Drawing List 2.xlsx')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)
              
from openpyxl import load_workbook

# workbook = load_workbook(filename='ST21_Drawing List 2.xlsx')
# wb = workbook.active
# print(sheet.nsheets)
# print(sheet.sheetnames)
# print(wb.get_sheet_names())

# Now you can read or write to the workbook
                            
print('file with xml extension'.center(80, "-"))
import xml.etree.ElementTree as ET
tree = ET.parse('xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

print('Exercise Level 1'.center(80, "-"))
print('Exercise 1'.center(80, "-"))

print(f'a) Read obama_speech.txt file and count number of lines and words')
import re
from collections import Counter

def count_rows_and_words_in_text(file_path):
    f = open(file_path) 
    lines = f.read().splitlines()
    print(f'The total rows in the file is {len(lines)}') #Count the total rows in the txt
    word_counts = 0
    for sentence in lines:
        regex_pattern = r'\b\w+\b' #\b to find a word boundary, \w to find one word character,+ means one or more times
        words = re.findall(regex_pattern, sentence)
        word_counts += len(words)
    print(f'The total words number is {word_counts}')
    f.close()

count_rows_and_words_in_text('./data/obama_speech.txt')

print(f'b) Read michelle_obama_speech.txt file and count number of lines and words')
count_rows_and_words_in_text('./data/michelle_obama_speech.txt')


print(f'c) Read donald_speech.txt file and count number of lines and words')
count_rows_and_words_in_text('./data/donald_speech.txt')


print(f'd) Read melina_trump_speech.txt file and count number of lines and words')
count_rows_and_words_in_text('./data/melina_trump_speech.txt')

print('Exercise 2'.center(80, "-"))
def find_top_languages(json_file_path, num): # num refer to how many numbers of the top
    with open(json_file_path, 'r', encoding = 'utf-8') as file:
        countries_data = json.load(file) #By using json.load() to load the file to dictionary
    # Argument : It takes file object as a parameter. Return : It return json object.
    #If it takes the list as input, it return a list also
    # print(type(countries_data))
    all_language = [language for country in countries_data for language in country['languages']]
    language_count = Counter(all_language)
    top_languages = language_count.most_common(num)
    reverse_top_languages = [(counts, language) for language, counts in top_languages]
    return reverse_top_languages

file_path = './data/countries_data.json'
top_num_languages = find_top_languages(file_path, 10)
print(top_num_languages)

file_path = './data/countries_data.json'
top_num_languages = find_top_languages(file_path, 3)
print(top_num_languages)


print('Exercise 3'.center(80, "-"))
print('Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries')
from collections import defaultdict
def most_populated_countries(json_file_path, num):
    with open(json_file_path, 'r', encoding = 'utf-8') as file:
        countries_data = json.load(file)
    country_population = {}
    country_population = [{'country':country['name'], 'population': country['population']} for country in countries_data]
    # for country in countries_data:
    #     country_population['country'] = country['name']
    #     country_population['population'] = country['population']
    sorted_country_population = sorted(country_population, key = lambda x: x["population"], reverse = True)
    print(sorted_country_population[:num])

most_populated_countries('./data/countries_data.json', 10)
most_populated_countries('./data/countries_data.json', 3)

'''
sample result
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]
'''

print('Exercise Level 2'.center(80, "-"))
print('Exercise 4'.center(80, "-"))
print(f'Extract all incoming email addresses as a list from the email_exchange_big.txt file.')
with open('./data/email_exchanges_big.txt') as file:
    txt = file.read()
    regex_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' #\.: matches the dot separating the domain name from the top-level domain (TLD)
    #No \ for first few character options: regex_pattern = r'[^A-Za-z]+' 
    email_address = re.findall(regex_pattern, txt)
    print(email_address)

print('Exercise 5'.center(80, "-"))
