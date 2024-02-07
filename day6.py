# Tuple unmodifiable,ordered collection
print("Exercise Level 1".center(80, "-"))
tuple_one = ()
tuple_sis = ("elder sis", "younger sis")
tuple_bro = ("elder bro", "younger bro")
siblings = tuple_sis + tuple_bro
print(siblings)
print(type(siblings))
print(len(siblings))

parents = ("Mom", "father")
family = parents + siblings
print(family)

family_list = list(siblings)  # Change Turple to list
family_list.append("Mom")
family_list.append("father")
print(family_list)
family_tuple = tuple(family_list)  # Change list to Turple
print(family_tuple)

print("Exercise Level 2".center(80, "-"))
print("Exercise 1".center(80, "-"))
# Unpack siblings and parents from family_members
print(f"{family_tuple = }")
siblings_list = family_tuple[:4]
parents_list = family_tuple[4:]
print(tuple(siblings_list))
print(tuple(parents_list))

print("Exercise 2".center(80, "-"))
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "pear", "banana")
vegetables = ("brocolli", "tomato", "celery")
animal = ("cat", "dog", "snake")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

print("Exercise 3".center(80, "-"))
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)

print("Exercise 4".center(80, "-"))
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp) % 2 != 0:
    index_middle_tp = int((len(food_stuff_tp) + 1) / 2)  # (9+1)/2 = 5
    middle_tp = food_stuff_tp[
        index_middle_tp - 1
    ]  # print[4] !! Print index dont forget to minus one
else:
    index_even_first_middle_tp = int(len(food_stuff_tp) / 2) - 1  # 10/2-1 = 4
    index_even_second_middle_tp = int(len(food_stuff_tp) / 2)  # 10/2 =5
    middle_tp = (
        food_stuff_tp[index_even_first_middle_tp]
        + food_stuff_tp[index_even_second_middle_tp]
    )
print(middle_tp)

print("Exercise 5".center(80, "-"))
# Slice out the first three items and the last three items from food_staff_lt list
first_three_food_stuff_list = food_stuff_list[0:3]
last_three_food_stuff_list = food_stuff_list[-3:]
print(first_three_food_stuff_list)
print(last_three_food_stuff_list)

print("Exercise 6".center(80, "-"))
# Delete the food_stuff_tp tuple completely
del food_stuff_tp

print("Exercise 7".center(80, "-"))
# Check if an item exists in tuple:Check if 'Estonia' is a nordic country.Check if 'Iceland' is a nordic country
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print(f"{'Estonia' in nordic_countries = }")
print(f"{'Iceland' in nordic_countries = }")
