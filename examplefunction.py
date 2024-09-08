"""Example Function"""

# Function
def square(number):
    return number ** 2

result = square(3)
print(result)

# Lambda funkcia
product = lambda x, y: x * y

result = product(4,5)
print(result)

# Decorators
def my_decoratos(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decoratos
def say_hello():
    print("Hello!")

say_hello()


import time

def timming_decorator(func):
    def wrapper(*args, **kwargs):


        star_time = time.time()
        print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(star_time))}")

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"End time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(star_time))}")

        total_time = end_time - star_time
        print(f"Total execution time: {total_time:.4f} seconds")

        return result
    return wrapper

@timming_decorator
def example_function(seconds):
    time.sleep(seconds)

example_function(2)

@timming_decorator
def greet():
    time.sleep(2)
    print("--Hello world")

greet()


# Example usage of abs()
negative_number = -10
absolute_value = abs(negative_number)
print(absolute_value)

# Example usage of divmond()
numerator = 17
denominator = 4
result = divmod(numerator, denominator)
print(result)

# round()
number = 5.678
rounded_number = round(number, 2)
print(rounded_number)

# Example usage of min()
print(min(10, 20,30))

# Example usage of max()
print(max(10, 20,30))

# Example usage of sum()
print(sum([1, 2, 3, 4, 5]))


# Example usage of complex()
print(complex(1, 2))


# Text manipulation
# Example usage of text()
number = 123
string_number = str(number)
print(string_number)

# Example usage of len()

text = "Hello, AI Engineers!"
lenght = len(text)
print(lenght)

# Example usage .upper()
print("Hello World".upper())

# Example usage .lower()
print("Hello World".lower())

# Example usage .capitalize()

print("helLo World".capitalize())

# Example usage of .find()
print("Hello World".find("World"))

# Example usage of .replace()
print("Hello World".replace("World", "Radovan"))

# Example usage of .startswith()
print("Hello World".startswith("Hello"))

# Example usage of .endswith()
print("Hello World".endswith("World"))

# Example usage of .strip()
print(" Hello World ".strip())

# Example usage of .lstrip()
print(" Hello World".lstrip())

# Example usage of .rstrip()
print("Hello World ".rstrip())

# Example usage of .split()
print("Hello World".split(" "))

# Example usage of .join()
print(" ".join(["Hello", "World"]))


# Type conversation
# Example usage of int()
float_number = 7.89
integer_number = int((float_number))
print(integer_number)

# Example usage of float()
integer_number = 5
floating_number = float(integer_number)
print(floating_number)

# Example usage of bool()
zero = 0
non_zero_number = 1
print(bool(zero))
print(bool(non_zero_number))

# Example usage od list(), tuple(), set(), and dict()
string = "Hello"
list_of_chars = list(string)
print(list_of_chars)

tuple_of_chars = tuple(string)
print(tuple_of_chars)

set_of_chars = set(string)
print(set_of_chars)

list_of_tuples = [('a', 1), ('b', 2)]
dict_from_list = dict(list_of_tuples)
print(dict_from_list)


# Data Structure Operations
# Example usage of max() and min()

numbers = [10, 20, 30, 40, 50]
max_value = max(numbers)
min_value = min(numbers)
print(max_value)
print(min_value)

# Example usage od sum()
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

# Example usage of sorted()

unsorted_list = [3, 1, 4, 1, 5, 9, 2]
sorted_list = sorted(unsorted_list)
print(sorted_list)

unsorted_list = [3, 1, 4, 1, 5, 9, 2]
sorted_list_reversed = sorted(unsorted_list, reverse = True)
print(sorted_list_reversed)

print("\r")

# Example usage of enumerate()
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

print("\r")
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")

# List method

## Create List
# Cerates new list with specifited elements.
my_list = [1, 2, 3]
print(my_list) 

## Append elements
#Adds an elements to the end of the list
my_list.append(4)
print(my_list)

## Insert elements
#Insert elements at a specific position in the list
my_list.insert(1, 'a')
print(my_list)

## Remove elements
# Remove the first occurrance of a specified element from the list
my_list.remove('a')
print(my_list)

## Pop element
# Removes and returns the last element of the list
print(my_list.pop)

## Find index
# Finds the index of the first occurrence of specified element in the list
print(my_list.index(2))

## Count element
# Counts the occurrences of a speciefed elemet in the list 
print(my_list.count(2))

## Sort list
# Sorts the elements of the list in acending order.
my_list.sort()
print(my_list)

## reverse list
# Reverses the order of the elements in the list 
my_list.reverse()
print(my_list)

## Get lenght
# Returns the numbers of elements in the list
print(len(my_list))

my_list[0] = 4
print(my_list)

# Set methods
 
## Create set
# Creates a new set from speciefed elements
my_set = {1, 2, 3}
print(my_set)

## Add element
# Adds an element to the set
my_set.add(4)
print(my_set)

## Remove element
# Removes a specief element from the set. Raises KeyError if the element is not defined
my_set.remove(2)
print(my_set)

## Discard element
# Removes an element from set the without raising an error if not defined
my_set.discard(3)
print(my_set)

## Union od set
# Returns a new set with all elements from both sets
union_set = my_set.union({2, 3})
print(union_set)

## Intersection of sets
# Returns a new set with elements coomon both sets
intersection_set = my_set.intersection({1, 2, 3})
print(intersection_set)

## Difference of sets
# Returns a new set with elements in my_set not in anothe_set
difference_set = my_set.difference({1, 4})
print(difference_set)

## Get lenght
# Returns the number of elements in the set 
print(len(my_set))


# Tuple methods

## Create Tuple
# Creates a new tuple with specified elements
my_tuple = (1, 'hello', 3.14)
print(my_tuple)

## Access element
# Accesses an element at a speciefed index in the tuple
print(my_tuple[1])

## Count elements 
# Counts the occurrences of a speciefed element in the tuple
print(my_tuple.count(1))

## Find index
# Finds index of the occurrences of a speciefed element in the tuple
print(my_tuple.index('hello'))

## Get lenght
# Returns the number of elements in the tuple
print(len(my_tuple))

## Unpack tuple
## Assings each element of the tuple to a separate variable

a, b, c = my_tuple
print(a, b, c)

# Dictionary methods

## Create dictionary
# Creates a new dictionary with speciefed key-value pairs
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict)

## Access value
# Accesses the value associated with speciefed key in the dictionary
print(my_dict['name'])

## Add/Update value
# Adds a new key-value pair or updates the value of an existing in the dictionary
my_dict['age'] = 26
print(my_dict)

my_dict['city'] = 'Prague'
print(my_dict)

## Remove key-value pair
# Removes a speciefed key-value pair from the dictionary
del my_dict['age']
print(my_dict)

## Get keys
# Returns a wiew of the keys in the dictionary
print(my_dict.keys())

## Get values
# Returns a view of values in the dictionary
print(my_dict.values())

## Get items
# Returns a view of key-values tuple pair in the dictionary
print(my_dict.items())

## get lenhgt
# Returns the number of key-value pairs in the dictionary
print(len(my_dict))

## Check existence of key
# Checks if a speciefed key exist in the dictionary
print('name' in my_dict)

## Get value with default
## Returns the value for a speciefed key in the dictionary, or a default value if the key is not found
print(my_dict.get('age', 0))

#Others

# Exampe usage of input()
name = input("Enter your name:")
print(f"Hello, {name}!")

# Example usage of open()
with open("/Users/radovan/Desktop/example.txt", "w") as file:
    file.write("Hello, AI Engineers")

with open("/Users/radovan/Desktop/example.txt", "r") as file:
    content = file.read()
    print(content)

# Logical operations

# Example usage of all()
conditions = [True, True, True]
print(all(conditions))

# Example usage of any()
conditions = [False, True, False]
print(any(conditions))

# Example usage of bool()
value = 0
print(bool(value))

value = 10
print(bool(value))


        
