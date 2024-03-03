#Web Scrapping

print("Catch up in Preview".center(80, "-"))
import requests #Package
from bs4 import BeautifulSoup #bs4 is a module, BeautifulSoup is a class

url = 'https://archive.ics.uci.edu/dataset/109/wine'

response = requests.get(url) #response is an instance of Response class, requests is a module, get() is a method of the module

#To check the status for opening the website
print(response.status_code) #instance.attribute of the response instance

#To check the website content
content = response.content
print(type(content)) #<class 'bytes'>
soup = BeautifulSoup(content, 'html.parser') #To create a BeautifulSoup object/instance called soup by parsing the content with 'html.parser'.
#Here soup is an instance/object. 
#syntax: soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title) #<title>UCI Machine Learning Repository</title>
print(soup.title.get_text()) #UCI Machine Learning Repository
print(soup.body) #Get the body of the part of the main content

'''
Typically to define a table in HTML
<table cellpadding="3">
    <tr>
        <td>Cell 1</td>
        <td>Cell 2</td>
    </tr>
    <!-- More rows and cells... -->
'''

print('\nstep1')
tables = soup.find_all('table')
print(tables)
print('\nstep2')
table = tables[0]
print(tables[0])


print("\nStep 3:")
#row extraction: to find all the rows within the tables
rows = table.find_all('tr')
print(type(rows)) #<class 'bs4.element.ResultSet'>

if rows: #If there are rows
    row_number = 1
    for row in rows:
        print(f'{row_number = }')
        cells = row.find_all('td') #To find all cells in the row
        if cells:
            for td in cells:
                print(td.text)
        else:
            print("No cells found in this row.")
        row_number += 1
else:
    print("No rows found in the table.")