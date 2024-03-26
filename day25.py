#Pandas


print("Catch up in Preview".center(80, "-"))

import pandas as pd
import numpy as np

print("Creating Pandas Series with Default Index".center(80, "-"))
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
'''
0    1
1    2
2    3
3    4
4    5
dtype: int64
'''
print("Creating Pandas Series with custom index".center(80, "-"))
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[6, 7, 8, 4, 5])
print(s)
'''
6    1
7    2
8    3
4    4
5    5
dtype: int64
'''

fruits = ['orange', 'banana', 'mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
'''
1    orange
2    banana
3     mango
dtype: objec
'''

print("Creating Pandas Series from a Dictionary".center(80, "-"))
dct = {'name':'Fang Ting',
       'country':'China',
       'city':'Shanghai'}

s = pd.Series(dct)
print(s)
'''
name       Fang Ting
country        China
city        Shanghai
dtype: object
'''

print("Creating a Constant Pandas Series".center(80, "-"))
s = pd.Series(10, index=[1, 2, 3])
print(s)
'''
1    10
2    10
3    10
dtype: int64
'''

print("Creating a Pandas Series using linspace".center(80, "-"))
s = pd.Series(np.linspace(5, 20, 10))
print(s)
'''
0     5.000000
1     6.666667
2     8.333333
3    10.000000
4    11.666667
5    13.333333
6    15.000000
7    16.666667
8    18.333333
9    20.000000
dtype: float64
'''

s = pd.Series(np.linspace(1.0, 5.0, num=10, endpoint=False))
print(s)
'''
0    1.0
1    1.4
2    1.8
3    2.2
4    2.6
5    3.0
6    3.4
7    3.8
8    4.2
9    4.6
dtype: float64
'''

#Format 1
print("Creating DataFrames from list of lists".center(80, "-"))
data = [
    ['Fangting', 'China', 'Shanghai'],
    ['KK', 'Malaysia', 'Ipoh'],
    ['John', 'Singapore', 'Jurong East']
    ]

dataframe = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(dataframe)
'''
       Name    Country         City
0  Fangting      China     Shanghai
1        KK   Malaysia         Ipoh
2      John  Singapore  Jurong East
'''

#Format 2
print("Creating DataFrames using Dictionary".center(80, "-"))
data = {'Name': ['Fangting', 'KK', 'John'],
        'Country': ['China', 'Malaysia', 'Singapore'],
        'City': ['Shanghai', 'Ipoh', 'Jurong East']
        }
df = pd.DataFrame(data)
print(df)
#Same output as format 1

#Format 3
print("Creating DataFrames from a list of Dictionaries".center(80, "-"))
data = [
        {'Name':'Fangting', 'Country':'China', 'City':'Shanghai'},
    {'Name':'KK', 'Country':'Malaysia', 'City':'Ipoh'},
    {'Name':'John', 'Country':'Singapore', 'City':'Jurong East'}
]
df = pd.DataFrame(data)
print(df)

print("Reading CSV file Using Pandas".center(80, "-"))
df = pd.read_csv(r'.\data\weight-height.csv')
print(df)

print("Data Exploration".center(80, "-"))
print(df.head(3)) #To read only the first 3 rows of the data, if no input then default it is first 5 rows
'''
  Gender     Height      Weight
0   Male  73.847017  241.893563
1   Male  68.781904  162.310473
2   Male  74.110105  212.740856'''

print(df.tail()) #default it is last 5 rows
'''
      Gender     Height      Weight
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103
'''

print(df.shape) #(10000, 3) #rows, columns

print(df.columns) #Index(['Gender', 'Height', 'Weight'], dtype='object')


print("Geting a specific column using the column key".center(80, "-"))
heights = df['Height']
print(heights)
'''
0       73.847017
1       68.781904
2       74.110105
3       71.730978
4       69.881796
          ...
9995    66.172652
9996    67.067155
9997    63.867992
9998    69.034243
9999    61.944246
Name: Height, Length: 10000, dtype: float64
'''
#It only will print first 5 and last 5 rows

weights = df['Weight']
print(weights)
'''
Name: Height, Length: 10000, dtype: float64
0       241.893563
1       162.310473
2       212.740856
3       220.042470
4       206.349801
           ...
9995    136.777454
9996    170.867906
9997    128.475319
9998    163.852461
9999    113.649103
Name: Weight, Length: 10000, dtype: float64
'''

print(len(heights)) #10000

print(heights.describe())
'''
count    10000.000000
mean        66.367560
std          3.847528
min         54.263133
25%         63.505620
50%         66.318070
75%         69.174262
max         78.998742
Name: Height, dtype: float64
'''

print(df.describe())
'''
             Height        Weight
count  10000.000000  10000.000000
mean      66.367560    161.440357
std        3.847528     32.108439
min       54.263133     64.700127
25%       63.505620    135.818051
50%       66.318070    161.212928
75%       69.174262    187.169525
max       78.998742    269.989699
'''

print("Modifying a DataFrame".center(80, "-"))

#To crreate a data set first
data = [
        {'Name':'Fangting', 'Country':'China', 'City':'Shanghai'},
    {'Name':'KK', 'Country':'Malaysia', 'City':'Ipoh'},
    {'Name':'John', 'Country':'Singapore', 'City':'Jurong East'}
]
df = pd.DataFrame(data)
print(df)

#Adding a new column
weights = [80, 50, 70]
df['Weight'] = weights
heights = [166, 160, 180]
df['Height'] = heights
print(df)

#Modifying column values
df['Height'] = df['Height'] * 0.01
print(df)

def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

df['BMI'] = bmi
df['BMI'] = round(df['BMI'], 1) #To round up an interger data by using round(x,1)

print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2024, index=[0, 1, 2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
'''
       Name    Country         City  Weight  Height   BMI  Birth Year  Current Year  Age
0  Fangting      China     Shanghai      80    1.66  29.0        1769          2024  255
1        KK   Malaysia         Ipoh      50    1.60  19.5        1985          2024   39
2      John  Singapore  Jurong East      70    1.80  21.6        1990          2024   34
'''

print("Checking data types of Column values".center(80, "-"))
print(df.Weight.dtype) #int64, Weight here is the index but without ''

print(df['Birth Year'].dtype) #Object

df['Birth Year'] = df['Birth Year'].astype('int') #To redefine the data type from object to int
print(df['Birth Year'].dtype) #int32

df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype) #int32

ages = df['Current Year'] - df['Birth Year']
df['Age'] = ages
print(df)

mean = (35 + 30) / 2
print('Mean', mean)

print(df[df['Age'] > 120]) 
#df['Age'] refer to one list of all the dataset, then df[xxx] will print all the data related to xx index

print(df[df['Age'] < 120 ])

print("Exercise 1~3".center(80, "-"))
print("Read the hacker_news.csv file from data directory, Get the first five rows & last five rows".center(80, "-"))

import pandas as pd

df = pd.read_csv('.\data\hacker_news.csv')

print("first 5 rows".center(80, "-"))
print(df.head())

print("Last 5 rows".center(80, "-"))
print(df.tail())


print("Exercise 4".center(80, "-"))
print("Get the title column as pandas series".center(80, "-"))
print(df['title'])


print("Exercise 5".center(80, "-"))
print(
    '''
Count the number of rows and columns
Filter the titles which contain python
Explore the data and make sense of it'''
.center(80, "-"))


print("To Filter the titles which contain python".center(80, "-"))
import re

#Method 1: To access the matched data one by one (Least preferred)
'''
for title in df['title']:
    regex_pattern = r'\b[Pp]ython\b'
    matches = re.search(regex_pattern, title)
    if matches is not None:
        print(df[df['title'] == title])
'''

#Method 2: To store the matches values and access them in the end by for loop (Still not so good)
matched_title = []

for title in df['title']:
    regex_pattern = r'\b[Pp]ython\b'
    matches = re.search(regex_pattern, title)
    if matches is not None:
        matched_title.append(title)

matched_df = df[df['title'].isin(matched_title)] #.isin() to judge the filtered title 
print(matched_df)

#Method 3: Straightly to judge for the dataframe (Best)
regex_pattern = r'\b[Pp]ython\b'
matched_df = df[df['title'].str.contains(regex_pattern, regex=True)]
print(matched_df)

