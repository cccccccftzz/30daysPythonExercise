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

'''
Import Libraries: Import necessary libraries, including requests for making HTTP requests, json for handling JSON data, webbrowser for opening web pages, and BeautifulSoup for web scraping.
Define URL: Set the URL of the webpage you want to scrape.
Make a Request: 
Web Scraping: Use BeautifulSoup to parse the HTML content of the webpage.
Extract Title: Extract and print the title of the webpage.
Find Facts Section: Locate the section containing Quick Facts & Stats.
Extract Hexagon Data: Extract data from hexagons, including labels and values.
Extract Facts Categories: Extract data from facts categories, including category names, item texts, and values.
Combine Data: Combine hexagon data and facts categories data into a single dictionary.
Convert to JSON: Convert the combined data dictionary to JSON format.
Save to File: Write the JSON data to a file named 'boston_university_facts.json'.
Print Status: Print a message indicating whether the facts section was found on the webpage.
This script essentially fetches information from a specific webpage, extracts relevant data, combines it, converts it to JSON format, and saves it to a file.
'''
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


print(f'Exercise 2'.center(80, "-"))
print('Extract the table in this url (https://archive.ics.uci.edu/dataset/882/large-scale+wave+energy+farm) and change it to a json file.')

import requests 
import json 
import webbrowser 

print('\nstep0: To get the file open and save the html to spot the data structure')
url = 'https://archive.ics.uci.edu/dataset/882/large-scale+wave+energy+farm'
response = requests.get(url)
print(response.status_code)

#Get the soup(content)
content = response.content
soup = BeautifulSoup(content, 'html.parser') #The 'html.parser' string refers to a specific parser module in Python that is used for parsing HTML

#Save the content as html for looking the HTML structure
with open('large-scale_wave_energy_farm.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify()) #To use prettify() method to get the formatted soup content, otherwise will come with <tag>
print(type(soup.prettify()))

#To get the title for the soup
print(soup.title) 
print(soup.title.get_text()) # instance.attribute.method()

print('\nstep1: Define a empty list to store all the dictionaries')
tables_data = []

print('\nstep2: To find the table header row and store in column_names')
header_row = soup.find_all('th')
column_names = [th.get_text() for th in header_row]
print(column_names)

print('\nstep3: To find the table data rows and store the data in a dictionary for every row')
data_row = soup.find_all('tr')[1:]
for row in data_row:
    table_data = {} #Define an empty dictionary to store one row data
    columns = row.find_all(['td'])
    for i in range(len(column_names)):
        table_data[column_names[i]]= columns[i].get_text() # Dont forget to use .get_text() to convert the html formatted text, , otherwise will come with <tag>
    tables_data.append(table_data) #Append one dictionary into the list, individual table_data as a dictionary

print('\nstep4: Convert the data to JSON')
# Convert the data to JSON
json_text = json.dumps(tables_data, indent=2, ensure_ascii=False)

print('\nstep4: Save the JSON data to a file')
with open('large-scale_wave_energy_farm.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_text)
print("Data saved as 'large-scale_wave_energy_farm.json'")


print(f'Exercise 3'.center(80, "-"))
print('''Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
The table is not very structured and the scrapping may take very long time.''')

'''
Part 1: To try some wikipediaapi existing function to get all the necessary info in wikipedia
including, check page exist, page titel, page summary, page URL.
'''

import wikipediaapi
import requests 
import re

#How To Get Single Page
wiki_wiki = wikipediaapi.Wikipedia('30_days_python_exercise (cft0627@gmail.com)', 'en')
page_py = wiki_wiki.page('List_of_presidents_of_the_United_States')

# To Check If Wiki Page Exists
print(f'Page - Exists: {page_py.exists()}') # Page - Exists: True

# To get Page title
print(f'Page - Title: {page_py.title}')

# To get Page Summary
print(f'Page - Summary: {page_py.summary[:100]}')

#How To Get Page URL
print(page_py.fullurl)

#How To Get Full Text (actually for this page, only can retrieve main structure)
wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='30_days_python_exercise (cft0627@gmail.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
p_wiki = wiki_wiki.page("List of presidents of the United States")

with open('wiki_List_of_presidents_of_the_United_States', 'w', encoding='utf=8') as text_file:
    text_file.write('Main Structure')
    text_file.write(p_wiki.text)


#How To Get Full HTML
wiki_html = wikipediaapi.Wikipedia(
    user_agent='30_days_python_exercise (cft0627@gmail.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
)
p_html = wiki_html.page("List of presidents of the United States")

with open('wiki_List_of_presidents_of_the_United_States.html', 'w', encoding='utf=8') as html_file:
    html_file.write(p_html.text)

#How To Get Page Sections
def print_sections(sections, level=0):
        for s in sections:
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
                print_sections(s.sections, level + 1)
print_sections(page_py.sections) #page_py = wiki_wiki.page('List_of_presidents_of_the_United_States')


# Part 2: To define a function to scrap the table inside the link
def scrape_presidents_data(url, output_html, output_json):
    """
    Scrapes data about the Presidents of the United States from a Wikipedia page.

    Parameters:
        - url (str): The URL of the Wikipedia page containing the data.
        - output_html (str): File path to save the HTML content for inspection. Default is 'List_of_presidents_of_the_United_States.html'.
        - output_json (str): File path to save the scraped data in JSON format. Default is 'presidents_data.json'.

    Returns:
        None

    The function sends a GET request to the provided URL, extracts the data from the first table in the HTML content,
    cleans up the header and row data, and saves the HTML content for inspection. The cleaned data is then stored in
    a JSON file.

    Example:
        scrape_presidents_data('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
    """
    
    print('\nstep0: To get the file open and save the html to spot the data structure')
    response = requests.get(url)
    print(response.status_code)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    with open(output_html, 'w', encoding='utf=8') as html_file:
        html_file.write(soup.prettify())

    # To locate the table
    table = soup.find_all('table', class_ ="wikitable sortable") #Table here is a list of one table, so the following table we used should be table[0]
    print(len(table)) #1 -> To confirm there is only one table

    print(f'step 1: Initialize an empty list to store the data')
    data = []

    print(f'step 2: Extract header row and clean the [xx] ref nos')
    header_row = [header.text.strip() for header in table[0].find('tr').find_all('th')] #To make sure find 'tr' first then find all 'th'
    for i in range(len(header_row)):
        header_row[i] = re.sub(r'\[.+\]', '', header_row[i]) # '.' means any character excep new line

    #Also can use the list comprehension below to combine two rows
    # header_row = [re.sub(r'\[.+\]', '', header.text.strip()) for header in soup.find('table', class_="wikitable sortable").find('tr').find_all('th')]

    '''
    header_row = [header.get_text() for header in table[0].find('tr').find_all('th')]
    This script .get_text() not good working
    .get_text() extracting the text content of an element.
    {
        "No.[a]\n": "1\n",
        "Portrait\n": "\n",
        "Name(Birth–Death)\n": "George Washington(1732–1799)[17]\n",
        "Term[14]\n": "April 30, 1789–March 4, 1797\n",
        "Party[b][15]\n": "\n",
        "Election\n": "Unaffiliated\n",
        "Vice President[16]\n": "1788–1789\n\n1792\n\n"
    },
    '''

    print(f'step 3: To extract the table data')
    for row     in table[0].find_all('tr')[1:]:  # [1:] skip the headrow
        row_data = [td.text.strip() for td in row.find_all(['th', 'td']) if 'style' not in td.attrs]

        #Clean the data including \n and [xx]
        for i in range(len(row_data)):
            row_data[i] = re.sub(r'\[.+\]', '', row_data[i])# Clean up all the "[xx]" reference numbers in the row data
            row_data[i] = re.sub(r'\n+', ' and ', row_data[i]) #\n means Newline, \n+ Replace one or more newlines

        data.append(dict(zip(header_row, row_data))) 

    print(f'step 4: Save data as JSON') 
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("JSON file has been created successfully.")

# To run the test link
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
output_html='List_of_presidents_of_the_United_States.html'
output_json='presidents_data.json'
scrape_presidents_data(url, output_html, output_json)

