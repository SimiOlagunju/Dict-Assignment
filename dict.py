
# Dictionary Assignment: 31-01-2022
#1. Use the get method to print the value of the "model" key of the car dictionary.

car =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print('SOLUTION TO QUESTION 1:')
print(car.get('model'))

#2. Which of the following are true of Python lists?
# A. All elements in a list must be of the same type
# B. A given object may appear in a list more than once
# C. A list may contain any type of object except another list
# D. These represent the same list:
# ['a', 'b', 'c']
# ['c', 'a', 'b']
# E. There is no conceptual limit to the size of a list

print('SOLUTION TO QUESTION 2:')
print('The following are true about Python LISTS: ' 'B C E')

#3. Create a dictionary that holds information of a user profile on twitter
user_profile = {
    'Username': 'Programmer.gh' ,
    'Age': 20,
    'Gender': 'Female',
    'Location': 'Ghana' ,
    'Passcode': 'icodeforaliving'
}
print('SOLUTION TO QUESTION 3:')

for k,v in user_profile.items():
    print(k,v)



























