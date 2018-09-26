"""
Data Structures: because sometimes we want to structure our data
This is done with several types of containers that help organize data in different ways

note: this is written as a series of interactive shell commands, not a runnable python file.
"""

# lists contain ordered arrangements of objects, in square brackets
string_list = ['apples', 'cinnamon', 'sugar', 'water']
int_list = [1, 3, 5, 2]
mixed_list = ['apples', 1, 'cinnamon', 3, 'sugar', 5, 'water', 2]
type(mixed_list)

# you make other things into lists by casting
list('applesauce')

# you can ask for information about the list
len(string_list) # length
5 in int_list # evaluate for truth

# The order of a list matters, because this order allows you to reference
# the data you store in a string through indexing (note: referencing endpoints is always exclusive)
start = string_list[0]
middle = int_list[3]
end = mixed_list[-2]
start
middle

#if you don't know the index of an item, you can ask for it
string_list.index('cinnamon')

# you can refer to parts of lists with slicing
string_list[:3]
int_list[3:]
mixed_list[1:4]

# if you're not sure how many items are in your list, you can ask for the length
length = len(mixed_list)
length
sub_length = len(mixed_list[2:5])
sub_length

# remember that order matters
mixed_list[length]  # error

"""
Lists are mutable, you can change them
"""
# adding and removing items 
## indexing and negative indexing 
string_list.append('crust')
int_list.append([2, 5, 7])
int_list
int_list[-1][2]

### if adding multiple items, you can use .extend to move the items to the end of the list.
nums = [1, 2, 3]
nums.append(2, 5, 7)

nums = [1, 2, 3]
nums.extend(8, 9, 10)
## output: [1,2,3,8,9,10]

string_list.remove('water')
int_list.remove(2)
string_list

# adding and removing items by index
del mixed_list[4]
mixed_list.insert(4, 'honey')
mixed_list

# reassigning items
int_list[2] = 8

# adding lists together
added_list = string_list + int_list
added_list

# you can change the order
mixed_list.sort()
string_list.sort(reverse=True)
int_list.reverse()

""" Tuples """
# Quick note: Tuples are like lists, but immutable (they can't be changed). They are in parentheses and more likely store different types of data
string_tuple = ('alpha', 'beta')
string_tuple.sort()  # error
sorted(string_tuple) # this returns a sorted list

# you can reference them the same way, but you can't reassign
string_tuple[1]
string_tuple[1] = 'gamma'  # error

"""
exercises
"""

# write a program that takes a list of names from the user and generates an invitation to each person to an event
# for instance:

# >>>Jackie, Ashley
# Jackie, you are cordially invited
# Ashley, you are cordially invited

# Increase the size of your list and print an invitation to the new invitees
# Remove the two invitees whose names start with letters latest in the alphabet, and inform them of the change
# Print the final count of invitees.
# pick one name to be your guest of honor. Move this person to the front of the list, followed by the rest of the invitees sorted alphabetically.
# print each name, one-at-a-time

"""
Dictionaries
"""
# Sometimes, you want to track not only data points, but also a label, or some other associated type of information
# Dictionaries let you reference data (or 'values') by labels (or 'keys'), instead of ordinal positions in a list.
# Note that Dictionaries are unordered, and each key must be unique

items = ['apples', 'cinnamon', 'sugar', 'water']
counts = [5, 2, 1, 2]
# we want these to stay paired, but lists are mutable. This can make them a  little squirrely when tying to coordinate
# between multiple lists. There's a better way!

# dictionaries come in curly brackets. Items (key:value pairs)in dictionaries are separated by commas
# {key1: value1, key2: value2, key3: value3...}
ingredients = {'apples': 5, 'cinnamon': 2, 'sugar': 1, 'water': 2}

# you can ask for information about dictionaries
len(ingredients)
'apples' in ingredients
5 in ingredients  # false: 'in ingredients' will look for keys

# or just certain properties of dictionaries
ingredients.keys()
ingredients.values()
5 in ingredients.values()
ingredients.items()  # this gives you a list of tuples

# the keys or values can be turned into a list: this is a good way to order them if you need to
list(ingredients.keys())
sorted(ingredients.values())
# sorted([(i, j) for i, j in ingredients.items()])

# you add items to dictionaries by assigning them- But no repeats!
ingredients['crust'] = 1
ingredients
ingredients['crust'] = 8
ingredients

# you can remove elements from a list by 'del'eting them
del ingredients['crust']
ingredients
# to empty a dictionary, reassign:
ingredients = {}

# any type of object (including data structures) can be values in a dict, but only strings or ints can be keys
ingredients['crust'] = ['butter', 'flour', 'water']
ingredients.values()
ingredients['bake time'] = {15: 'bottom crust', 30: 'whole pie', 'egg wash': 5}
ingredients.values()
ingredients[('sweet', 'spicy')] = 'allspice'  # error: tuples can't be keys

""" SETS """
# Quick Note: sets are a lot like dictionaries without values. They're immutable, unordered, and have unique values.
# They can be used for set-logical operaations, like intersections and unions, and are often more efficient than lists
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set3 = set1 & set2  # Intersection
set4 = set1 | set2  # Union
set5 = set1 - set2  # Difference

# sets are unordered, and therefore do not support indexing, but you can check for membership
set1[0]  # error
2 in set1  # True

"""
Exercises
"""
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.
# Replace the value for the city in which the person lives with a list of all the places they've ever lived.
# create another dictionary with the same information for another friend, and combine the two into a single dictionary
# Print the names and ages of your friends


"""
Final note: For more resources, python documentation on built-in types is available at
https://docs.python.org/3/library/stdtypes.html

For those who are unfamiliar with stack overflow, it's a massive community-sourced forum for programming questions.
Whatever your question is, it has probably been asked before, and there is probably an answer on stack overflow.
"""

