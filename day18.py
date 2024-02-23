#Regular Expressions

# import day10
# print(day10.reverse_fruits)
#This is testing the import other module entirely

print("Catch up in Preview".center(80, "-"))

import re

print("Match".center(80, "-"))
#re.match(substring, string, re.I)
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span) #(0,15)

start,end = span
print(start, end) #0 15

substring = txt[start:end]
print(substring) #I love to teach

match = re.match('to teach', txt, re.I)
print(match) # Return None, because the string is not starts with the substring

'''
The difference between Match and Search
The match function returns an object only if the text starts with the pattern.
search is much better than match because it can look for the pattern throughout the text. 
'''

print("Search".center(80, "-"))
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)

print('One and more times (+)'.center(80, "-"))
regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d+'
matches = re.findall(regex_pattern, txt)
print(matches)

print('Period(.)'.center(80, "-"))
regex_pattern = r'[a].'
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches) #['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'
matches = re.findall(regex_pattern, txt)
print(matches) #['and banana are fruits']

regex_pattern = r'[a]..'
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches) #['and', 'ana', 'a a'] To output 3 characters

regex_pattern = r'[a]..+'
matches = re.findall(regex_pattern, txt)
print(matches) #['and banana are fruits']
#Because + alr mean one or more times, so no need double '.'

print('Zero or one time (?)'.center(80, "-"))
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
#Multi-line string can be defined in  '''

regex_pattern = r'[Ee]-?mail' # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)

print('Quantifier in RegEx'.center(80, "-"))
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}' #Digits but exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)

print('Cart ^'.center(80, "-"))
#Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This' #^Means the whole string starts with XXX then print out the matches 
matches = re.findall(regex_pattern, txt)
print(matches)

#Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z]+' 
# ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)

print('Exercise Level 1'.center(80, "-"))
print('Exercise 1'.center(80, "-"))

print('Method 1 - Using string replace, split then count by defaultdic'.center(80, "-"))

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

#To replace all '.' with empty string ''
modified_paragraph = paragraph.replace('.', '')
# print(modified_paragraph)

#Split the sentence into individual word
split_paragraph = modified_paragraph.split()
# print(split_paragraph)

#To get list of turple

#To use defaultdict to count the appearance time
from collections import defaultdict

output_dic = defaultdict(int)
for word in split_paragraph:
    # print(word)
    output_dic[word] += 1

# print(output_dic)

sort_dic = {k: v for k, v in sorted(output_dic.items(), key = lambda item: item[1], reverse=True)} 
# Here the format to create ta dictionary

sort_lst = [(v, k) for k, v in sorted(output_dic.items(), key = lambda item: item[1], reverse=True)]
print(sort_lst)
# Here to create a list of tuple

print('Method 2 - using re'.center(80, "-"))
import re
from collections import Counter

regex_pattern = r'\b\w+\b' 
'''
r'' to declare a regax variable
\b to find a word boundary
\w to find one word character
+ means one or more times
'''
words = re.findall(regex_pattern, paragraph)
print(words)

word_counts = Counter(words)
print(word_counts)

most_common_words = word_counts.most_common() #To use the .most_common function

#To reverse the word and count sequence
most_common_words = [(word, count) for count, word in most_common_words ]
print(most_common_words)

print('Exercise 2'.center(80, "-"))
print('''The position of some particles on the horizontal x-axis 
      are -4, -12, -3 and -1 in the negative direction, 
      0 at origin, 4 and 8 in the positive direction. 
      Extract these numbers from this whole text 
      and find the distance between the two furthest particles.'''
)

txt = 'Particle at x = -4, -12, -1, and -3 in the negative direction, with the origin at x = 0. Moving in the positive direction, there are particles located at x = 8 and x = 4. This arrangement represents their respective positions along the axis, with negative values indicating positions to the left of the origin and positive values indicating positions to the right.'

regex_pattern = r'-?\d+'
points = re.findall(regex_pattern, txt)
print(points)

int_points = [int(value) for value in points ]
int_points.sort()
print(int_points)
print(f'distance = {int_points[-1]} - {int_points[0]} = {int_points[-1] - int_points[0]}')

print('Exercise Level 2'.center(80, "-"))
print('Exercise 2'.center(80, "-"))
print('Write a pattern which identifies if a string is a valid python variable')
def is_valid_variable(txt):
    regex_pattern = r'^\d'
    matches = re.match(regex_pattern, txt) 
    if '-' in txt:
        return False
    elif matches is not None:
        return False
    else: 
        return True
    
    
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('first-name'))
print(is_valid_variable('first_name'))
print(is_valid_variable('firstname'))

print('Exercise 3'.center(80, "-"))
print('Clean the following text. After cleaning, count three most frequent words in the string.')

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_sentence = re.sub('[!@#$%^&;]', '', sentence)
print(cleaned_sentence)

words = re.findall(r'\b\w+\b', cleaned_sentence)
print(words)

def most_frequence_words(txt):
    word_counts = Counter(txt)
    # print(word_counts)
    most_common_words = word_counts.most_common() #To use the .most_common function
    return most_common_words[0:3]

print(most_frequence_words(words))