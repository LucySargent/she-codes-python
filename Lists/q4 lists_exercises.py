# Using the following starter code
# Produce the following lists
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

# d = []
# # list1.insert(0,a)        OUTPUT [[1, 2, 3]]
# # list1.insert([0,a][1,b]) TypeError: list indices must be integers or slices, not tuple
# # list1.extend(a)          OUTPUT [1, 2, 3]
# d.extend([a,b,c])          # CORRECT OUTPUT [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(d)

list_e = []
# list_e.extend(a,b,c)      OUTPUT: TypeError: list.extend() takes exactly one argument (3 given)
list_e = a + b + c          #CORRECT OUTPUT [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_e)
 
