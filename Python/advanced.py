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

