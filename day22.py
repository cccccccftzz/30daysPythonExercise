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

print(f'Exercise 1'.center(80, "-"))
print('Scrape the following website and store the data as json file(url = \'http://www.bu.edu/president/boston-university-facts-stats/\').')

import requests
import json
import webbrowser

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
print(response.status_code)
# webbrowser.open_new_tab(url) #in any default webbrowser

content = response.content
soup = BeautifulSoup(content, 'html.parser') 
#Here soup is an instance/object. 
#syntax: soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)  #<title>BU Facts &amp; Stats | Office of the President</title>
print(soup.title.get_text())  #BU Facts & Stats | Office of the President
# print(soup.body)

print('\nstep1')
# Find the section containing Quick Facts & Stats
facts_section = soup.find('section', class_='facts-stats') #Subsection

if facts_section:
    # Extract data from hexagons
    hexagons = facts_section.find_all('div', class_='hexagon') #Sub-Subsection 1
    
    hexagon_data = []
    for hexagon in hexagons:
        value = hexagon.find('h2').text.strip()
        label = hexagon.find('h4').text.strip()
        hexagon_data.append({'label': label, 'value': value})

    # Extract data from facts categories
    facts_categories = soup.find_all('div', class_='facts-wrapper') #Sub-Subsection 2
    # print(facts_categories) #This row used to check whether scrap the subsubsection successfully

    facts_data = {}
    for category in facts_categories:
        category_name = category.find('h5').text.strip()
        category_items = category.find_all('li', class_='list-item')
        
        category_values = {}
        for item in category_items:
            text = item.find('p', class_='text').text.strip()
            value = item.find('span', class_='value').text.strip()
            category_values[text] = value

        facts_data[category_name] = category_values

    # Combine both sets of data
    result_data = {'hexagons': hexagon_data, 'categories': facts_data}

    # Convert the data to JSON
    json_text = json.dumps(result_data, indent=2, ensure_ascii=False)

    # Save the JSON data to a file
    with open('boston_university_facts.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_text)

    print("Data saved as 'boston_university_facts.json'")
else:
    print("Facts section not found on the webpage.")