# 0. Making Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
#<------------------------------------------------------------------------->
# 1.Clear the dictionary
my_dict.clear()
print(my_dict)
#<------------------------------------------------------------------------->
# 2.Copy the dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
# Create a copy of the dictionary
new_dict = my_dict.copy()
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}
print(new_dict)
#<------------------------------------------------------------------------->
# 3.Fromkeys Create a dictionary with keys 'a', 'b', 'c', and default value 0
my_dict = dict.fromkeys(['a', 'b', 'c'], 0)
# Output: {'a': 0, 'b': 0, 'c': 0}
print(my_dict)
#<------------------------------------------------------------------------->
# 4. get Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
# Get the value of the 'name' key
name = my_dict.get('name')
# Output: 'John'
print(name)
# Try to get the value of a non-existent key
non_existent_value = my_dict.get('occupation', 'Not found')
# Output: 'Not found'
print(non_existent_value)
#<------------------------------------------------------------------------->
# 5. items Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Get a list of key-value pairs
items_list = my_dict.items()
# Output: dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])
print(items_list)
#<------------------------------------------------------------------------->
# 6. Keys Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Get a list of keys
keys_list = my_dict.keys()
# Output: dict_keys(['name', 'age', 'city'])
print(keys_list)
#<------------------------------------------------------------------------->
# 7.pop Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Pop the 'age' key and get its value
age = my_dict.pop('age')
# Output: 25
print(age)
# Output: {'name': 'John', 'city': 'New York'}
print(my_dict)
#<------------------------------------------------------------------------->
# 8. popitem Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# Pop the last inserted item
last_item = my_dict.popitem()
# Output: ('city', 'New York')
print(last_item)
# Output: {'name': 'John', 'age': 25}
print(my_dict)
#<------------------------------------------------------------------------->
# 9. setdefault Original dictionary
my_dict = {'name': 'John', 'age': 25}
# Get the value of the 'city' key, and insert it with the default value 'Unknown' if it doesn't exist
city = my_dict.setdefault('city', 'Unknown')
# Output: 'Unknown'
print(city)
# Output: {'name': 'John', 'age': 25, 'city': 'Unknown'}
print(my_dict)
#<------------------------------------------------------------------------->
# 10. Update Original dictionary
my_dict = {'name': 'John', 'age': 25}
# Update the dictionary with a new key-value pair
my_dict.update({'city': 'New York'})
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)
#<------------------------------------------------------------------------->