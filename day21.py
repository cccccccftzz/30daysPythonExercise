#Classes and objects

print("Catch up in Preview".center(80, "-"))

#Everything in Python is a class

print('Creating a class'.center(80, "-"))
#Creating a class
class Person:
    pass
print(Person)

print('Creating an instance of the class'.center(80, "-"))
#Creating an instance of the class
person_instance = Person()
print(person_instance)

print('Creating an object'.center(80, "-"))
p = Person()
print(p)


print('Class Constructor'.center(80, "-"))
class Person:
    def __init__(self, name, age): # __init__ is the Constructor, name, age.. is the attributes to class
        self.name = name
        self.age = age

person_one = Person('Fang Ting', 55)
person_two = Person('lx', 99)
print(person_one) #Instance
print(person_one.name)
print(person_one.age)

print('Define Object Methods'.center(80, "-"))
class Person:
    def __init__(self, firstname, lastname, age, country, city): #More parameters for constructor function
        self.age = age
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.city = city
    def person_info(self): #Define a method (function) to the Objects
        return f'{self.firstname} {self.lastname} is {self.age}. She lives in {self.city}, {self.country}.'

person_one = Person('FangTing', 'Chen', 18, 'China', 'Shanghai')
print(person_one.person_info()) #instance/objects.method

'''
person_two = Person()
print(person_two.person_info()) TypeError: Person.__init__() missing 5 required positional arguments: 'firstname', 'lastname', 'age', 'country', and 'city'
'''

print('Object Default Methods'.center(80, "-"))
class Person:
    def __init__(self, firstname = 'Fang Ting', lastname = 'Chen', age = '18', country = 'China', city = 'Shanghai'):
        #define the par
        self.age = age
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.city = city
    def person_info(self): #Define a method (function) to the Objects
        return f'{self.firstname} {self.lastname} is {self.age}. He/She lives in {self.city}, {self.country}.'

person_one = Person() #No given info when creating the instance, also can created successfully
print(person_one.person_info()) #Fang Ting Chen is 18. She lives in Shanghai, China.

# john = Person('lx', 'Yuan', age = 30, 'Singapore', 'Singapore')
#Cannot work. Once giving the key, the following arguments should be followed by the key name also
john = Person('lx', 'Yuan', age = 30, country = 'Singapore', city = 'Singapore')
print(john.person_info())

print('Method to Modify Class Default Values'.center(80, "-"))
class Person:
    def __init__(self, firstname = 'Fang Ting', lastname = 'Chen', age = '18', country = 'China', city = 'Shanghai'):
        #define the par
        self.age = age
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.city = city
        self.skills = []
    def person_info(self): #Define a method (function) to the Objects
        return f'{self.firstname} {self.lastname} is {self.age}. He/She lives in {self.city}, {self.country}.'
    def add_skill(self, skill): #Define a mthod to modify a attributes of the class
        self.skills.append(skill)

person_one = Person()
print(person_one.person_info()) #Fang Ting Chen is 18. He/She lives in Shanghai, China.

person_one.add_skill('Python')
person_one.add_skill('Structral Design')
print(person_one.skills) #['Python', 'Structral Design']
 
""" 
print(person_one.skills()) 
wrong, skills is an attribute already, not a method, so no need add '()'
"""
person_two = Person('lx', 'Yuan', '30', 'Malaysia','JB')
print(person_two) #Instance only , <__main__.Person object at 0x0000014109072C00>
print(person_two.person_info()) #lx Yuan is 30. He/She lives in JB, Malaysia.
print(person_two.skills) # [] empty, cuz not assigned

print('Inheritance'.center(80, "-"))
#syntax: Class inherited Class(Parent Class)
class Student(Person): 
    pass

student_one = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
print(student_one.person_info()) #person_info is the method of the parent Class
print(student_one.skills) #[], Here still not yet given any values to skills
student_one.add_skill('Javascripts') 
student_one.add_skill('React')
print(student_one.skills)  #['Javascripts', 'React']

print('Overriding parent method'.center(80, "-"))
class Student(Person): 
    def __init__(self, firstname = 'Fang Ting', lastname = 'Chen', age = '18', country = 'China', city = 'Shanghai', gender = 'Female'):
        self.gender = gender #Give a new attribute which not in the parent classes' Constructor
        super().__init__(firstname, lastname, age, country, city) 
        '''
        super() built-in function:
        To copy the attributes default value from the parent class instead of repeating here
        '''
    def person_info(self): #Define a method (function) to the Objects
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age}. {gender} lives in {self.city}, {self.country}.'

student_one = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male') #Case senstive, dont forget to follow the small captial which is defined in the conditions above
print(student_one.person_info()) #Eyob Yetayeh is 30. He lives in Helsinki, Finland.

print('Exercise Level 1'.center(80, "-"))

class Stat:
    def __init__(self, lst) -> None:
        self.lst = lst

    def count(self):
        return len(self.lst)
    
ages =[1,2]
my_stat = Stat(lst=ages)
print(my_stat.count())



class HDB():
    def __init__(self, levels, name):
        self.levels = levels
        self.name = name
    
    def get_max_people(self):
        return self.levels * 10
    
puggol_hdb = HDB(5, "puggol")
hougang_hdb = HDB(10, "hougang")

print(puggol_hdb.get_max_people())
print(hougang_hdb.get_max_people())

print('Exercise 1'.center(80, "-"))
#Define the class

import statistics
from collections import Counter

class Statistics:
    def __init__(self, lst):
        self.lst = lst
        
    def count(self):
        return len(self.lst)
    
    def sum(self):
        return sum(self.lst)
    
    def min(self):
        return min(self.lst)
    
    def max(self):
        return max(self.lst)
    
    def range(self):
        return max(self.lst) - min(self.lst) 
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        return statistics.median(self.lst) #Here statistics all in lower case represents the module/script.method
    
    def mode(self):
        return statistics.mode(self.lst)
    
    def std(self):
        return statistics.stdev(self.lst)

    def var(self):
        return statistics.variance(self.lst)

    def freq_dist(self):
        num_count = Counter(self.lst)
        fre_num = [(100 * count/self.count(), num) for num, count in num_count.items()]
        fre_num_sorted = sorted(fre_num, key=lambda x: x[0], reverse=True)
        return fre_num_sorted

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(lst = ages)
print(f'{data.count() = }')
print(f'{data.sum() = }')
print(f'{data.min() = }')
print(f'{data.max() = }')
print(f'{data.range() = }')
print(f'{data.mean() = }')
print(f'{data.median() = }')
print(f'{data.mode() = }')
print(f'{data.std() = }')
print(f'{data.var() = }')
print(f'{data.freq_dist() = }')

print('Exercise 2'.center(80, "-"))

class Income:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

class Expense:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes # List[Income]
        self.expenses = expenses # List[Expense]]
        
    def total_income(self):
        return sum(income.amount for income in self.incomes)

    def total_expense(self):
        return sum(expense.amount for expense in self.expenses)

    def account_info(self):
        return f'Full Name: {self.firstname} {self.lastname}\nAccount Balance: {self.account_balance()}'
    
    def add_income(self, amount, description):
        self.incomes.append(Income(amount,description)) 
        #To append into the list as an Income instance

    def add_expense(self, amount, description):
        self.expenses.append(Income(amount,description))
    
    def account_balance(self):
        balance = self.total_income() - self.total_expense()
        return balance

#Tester
my_incomes = [Income(1000, "salary"), Income(500, "bonus")] #list of income instances
my_expenses = [Expense(300, 'transportation'), Expense(100, 'Food'), Expense(200, 'Beauty')]
person_one = PersonAccount('Fang Ting', 'Chen', my_incomes, my_expenses)

print(person_one.account_info()) 
# Full Name: Fang Ting Chen
# Account Balance: 900
print(person_one.account_balance()) #900

person_one.add_income(400, 'Stocks')
person_one.add_expense(100, 'Utilities')

print(person_one.account_info())
#Full Name: Fang Ting Chen
# Account Balance: 1200
print(person_one.account_balance()) #1200