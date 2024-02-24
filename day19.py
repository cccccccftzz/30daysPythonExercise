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
