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


