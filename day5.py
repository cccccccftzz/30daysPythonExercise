# List
print("Exercise Level 1".center(80, "-"))
print("Exercise 1".center(80, "-"))
# Declare an empty list
lst = []
print(lst)
print(type(lst))
lst = list()
print(lst)
print(type(lst))

print("Exercise 2~4".center(80, "-"))
# Declare a list with more than 5 items
lst = ["abc", "bc", "dce", "efaedf", "lpt", "aoe"]
print(lst)
print(len(lst))
first_item_lst = lst[0]
second_item_lst = lst[1]
last_item_lst = lst[-1]
print(first_item_lst)
print(second_item_lst)
print(last_item_lst)

print("Exercise 5".center(80, "-"))
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Fang Ting", "30", "166", "Single", "500 Beach Rd"]
print(mixed_data_types)

print("Exercise 6~12".center(80, "-"))
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[1])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[3] = "Lazada"
print(it_companies)

it_companies.append("Grab")
print(it_companies)

it_companies.insert(1, "Tiktok")
print(it_companies)

print("Exercise 13".center(80, "-"))
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

print("Exercise 14".center(80, "-"))
# Join the it_companies with a string '#;  '
print("#".join(it_companies))

print("Exercise 15".center(80, "-"))
# Check if a certain company exists in the it_companies list.
company_search = "Shoppee"
print(
    f'{company_search} {'is' if company_search in it_companies else 'is not'} in the IT company list'
)

print("Exercise 16".center(80, "-"))
# Sort the list using sort() method
print(it_companies)
sort_it_companies = it_companies.sort()
print(sort_it_companies)
print(it_companies.sort())
"""
Cannot work, after the original list is modified, 
The sort() is not a new sorted list and no value to be assigned to the new list.
Same as using print () function
The correct way to sort() is as shown below
"""

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

print("Exercise 17".center(80, "-"))
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

print("Exercise 18~20".center(80, "-"))
# Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = it_companies[0:3]  # slice first three, 0,1,2 not [0:4]
print(it_companies)

# Slice out the last 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = it_companies[-3:]
print(it_companies)

# Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = it_companies[2:-2]  # [2:-2] also can work!!!
print(it_companies)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = it_companies[2:5]
print(it_companies)

print("Exercise 21~25".center(80, "-"))
# Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[2:-2]
print(it_companies)

# Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
# del it_companies
# print(it_companies)

print("Exercise 26".center(80, "-"))
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_Stack = front_end + back_end
full_Stack.append("python")
full_Stack.append("SQL")
print(full_Stack)

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
# The following is a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])
# print ((len(ages) + 1) / 2 if len(ages) % 2 != 0 else len(ages) / 2)  # Once using "/" the result always to be float!!
# index_of_median_age = int( (len(ages) + 1) / 2 if len(ages) % 2 != 0 else len(ages) / 2 )
if len(ages) % 2 != 0:
    index_odd_median_age = int((len(ages) + 1) / 2)
    median_age = ages[index_odd_median_age]
else:
    index_even_first_median_age = int(len(ages) / 2)
    index_even_second_median_age = int(len(ages) / 2) + 1
    median_age = (
        ages[index_even_second_median_age] + ages[index_even_first_median_age]
    ) / 2
print(f"{median_age = }")

print(6 / 3)  # Once using "/" the result always to be float!!

# Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sum_nos_of_ages = sum(ages)
total_people_no = len(ages)
average_age = sum_nos_of_ages / total_people_no
print(f"{average_age = }")

# Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0])
print(ages[-1])
range_of_ages = ages[-1] - ages[0]
print(f"{range_of_ages = }")

# Compare the value of (min - average) and (max - average), use abs() method
print(type(ages[0]))
print(type(average_age))
min_minus_average = abs(ages[0] - average_age)
mas_minus_average = abs(ages[-1] - average_age)
print(
    f'The (min-average) {'is' if min_minus_average > mas_minus_average else 'is not'} bigger than (max-average)'
)

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
# Find the middle country(ies) in the countries list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

if len(countries) % 2 != 0:
    index_odd_middle_country = int((len(countries) + 1) / 2)
    print(countries[index_odd_middle_country])
else:
    index_even_first_median_age = int(len(countries) / 2)
    index_even_second_median_age = int(len(countries) / 2) + 1
    print(
        countries[index_even_first_median_age], countries[index_even_second_median_age]
    )

print("Exercise 2".center(80, "-"))
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(len(countries))
if len(countries) % 2 == 0:
    length_first_batch_of_country = int(len(countries) / 2)  # 6/2=3
    countries_one = countries[:length_first_batch_of_country]  # [:3]
    countries_two = countries[length_first_batch_of_country:]  # [3:]
else:
    length_first_batch_of_country = int((len(countries) + 1) / 2)  # (7+1)/2 = 4
    print(length_first_batch_of_country)
    countries_one = countries[:length_first_batch_of_country]  # [:4]
    countries_two = countries[length_first_batch_of_country:]  # [4:]
print(f"{countries_one = }")
print(f"{countries_two = }")

print("Exercise 3".center(80, "-"))
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_three = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
first_countries, second_countries, third_countries, *scandic_countries = countries_three
print(f"{first_countries = }")
print(f"{second_countries = }")
print(f"{third_countries = }")
print(f"{scandic_countries = }")
