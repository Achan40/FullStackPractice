# List comprehension basics
mat = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [i[0] for i in mat]
print(first_col)

# Dictionaries 
mystuff = {"key1":123,"key2":'val2',"key3":{'123':[1,2,'grabMe']}}
print(mystuff['key3']['123'][2])

# Sets : only contain unique elements
x = set()
x.add(1)
x.add(2)
x.add(2)

print(x)


# Regular Expressions
import re

patterns = ["term1", "term2"]
text = 'This is is a string with term1, not the other'

for pattern in patterns:
    print("I'm searching for: " + pattern)

    # Using regular expressions to determine if pattern in text, returns match object
    if re.search(pattern, text):
        print("Match!")
    else:
        print("No Match")

# Returns integer for location of term
match = re.search('term1',text)
print(match.start())

# Splitting terms
split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term,email))

# Find all instances of a pattern in a string
print(re.findall('match', 'test phrase match in middle match'))

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = "sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd"

# Want to find an s followed by zero or more d's,
test_patterns = ['sd*']

multi_re_find(test_patterns,test_phrase)

# Want to find an s followed by one or more d's,
test_patterns = ['sd+']
multi_re_find(test_patterns,test_phrase)

# Want to find an s followed by zero or one d's,
test_patterns = ['sd?']
multi_re_find(test_patterns,test_phrase)

# Want to find an s followed by n d's,
test_patterns = ['sd{3}']
multi_re_find(test_patterns,test_phrase)

# Want to find an s followed by m or n d's,
test_patterns = ['sd{1,3}']
multi_re_find(test_patterns,test_phrase)

# Want to find an s followed by one or more s's or one or more d's,
test_patterns = ['s[sd]+']
multi_re_find(test_patterns,test_phrase)

# Removing punctuation
test_phrase = 'This is a string! But it has punctuation, How can we remove it?'
test_patterns = ['[^!,?]+']
multi_re_find(test_patterns,test_phrase)
# There is must more that these as well

# Importing custom modules
import this_is_a_module
this_is_a_module.func_in_module()


# Decorators
# Functions that modify the functionality of other functions

# Returning Functions
def hello(name="Aaron"):
    print("The hello() function has been run")

    def greet():
        return "This string is inside greet()"

    def welcome():
        return "This string is inside welcome()"

    # Returning functions
    if name == "Aaron":
        return greet
    else:
        return welcome

x = hello()

print(x())

# Function as an arguement
def hello():
    return "Hi Aaron"

def other(func):
    print("Hello")
    print(func())

other(hello)

# Creating decorators
def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("func() has been called")
    
    return wrap_func

def func_needs_decorator():
    print("This funtion is in need of a decorator")

# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

# Instead of doing the above lines we can do this
@new_decorator
def func_needs_decorator():
    print("This funtion is in need of a decorator")

func_needs_decorator()