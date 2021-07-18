#1.Write a function that takes a temp in fahrenheit and returns the temp in celsius

# def convert_f_to_c(temp_in_f):
#     convert_f_to_c = (temp_in_f - 32) *5/9
#     return convert_f_to_c
# print(convert_f_to_c(40))

# farenheit to celsius
# def convert_c_to_f(temp_in_c):
#     convert_c_to_f = (temp_in_c * 9/5) +32
#     return convert_c_to_f
# print(convert_c_to_f(0))

#2.Write a function that accepts one parameter(an integer)
# and returns True when parameter is odd 
# and returns False when parameter is even

# def is_it_odd(num):
#     if num %2 == 0:
#         return False
#     else:
#         return True
# print(is_it_odd(7))

#3> Write a function that returns the mean of a list of numbers

# def mean(num_list):
#     return sum(num_list) /len(num_list)
# # print(mean([4,3,2,6]))
# print(mean([10,5,6]))

# 4.write a function that takes two perameters:
# the unit price of an item 
# how many units were purchased
# return total cost as a string

#v1
# def total_cost(unit_price,quantity):
#     total_cost = unit_price * quantity
#     return total_cost
# print(total_cost(3,3))

#v2
# def total_cost(unit_price,quantity):
#     total_cost = unit_price * quantity
#     return total_cost
# print(f"${total_cost(4.25,3)}")

#v3
# def total_cost(price,quantity):
#     return price * quantity
# print(f"${total_cost(4.25, 3)}")

