# def my_function(lucy,asli): #lucy = "123", lucy ="asli"
#     greetings = "Lucy said " + asli
#     return greetings

# print(my_function("123","hello"))

##############

# def name(title,fname,lname):
#     greeting = "Hello " + title + fname + lname
#     return greeting

# print(name("Lady ", "Lucy " ,"Sargent"))

##############
# https://www.w3resource.com/python-exercises/python-functions-exercises.php 

# def max_of_two(x,y):
#     if x > y:
#         return x
#     else:
#         return y
# print(max_of_two(5,10))

##############

# def max_of_three(x,y,z):
#     return(max(x,y,z))
# print(max_of_three(1,2,3))

############## sum numbers

# def calc_sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return(total)
# print(calc_sum((1,2,3,4,5,1,4,5)))

# numbers = [1,2,3,4,5,1,4,5]  ##not using a function
# # sum = sum(numbers)
# # print(sum)

# sum = sum(numbers, 10)
# print(sum)

############## multiply numbers in a list

# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return(total)
# print(multiply((10,2)))

############## divide two numbers

# def quotient(a,b):
#     return a/b
# print(quotient(10,5)) # returns float

############## divide two numbers

# def quotient(a,b):
#     return a/b
# print(int(quotient(10,5)))  #returns integer

############## reverse a string

# def rev_string(text):
#     return text[::-1]
# # print(rev_string("Lucy"))
# print(rev_string("1234abcd"))

############## reverse a string

# def string_rev(mystring):
#     revstring = ''
#     index = len(mystring)
#     while index > 0:
#         revstring += mystring[index - 1]
#         index = index - 1
#     return  revstring 
# print(string_rev("lucy"))

############## return a factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factorial: "))
# print(factorial(n))


############## check is a number fals in a given range
# def range_check(n):
#     if n in range(-10,10):
#         print(" %s is in the given range" %str(n))
#     else:
#         print("The number is outside the given range.")
# range_check(5)

############## .format

# text = "Milie is {age} years old"
# print(text.format(age = 11))

############## index()
# txt = "lucy jane sargent"
# x = txt.index("jane")
# print(x)

############## print even numbers from list

# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum    
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

############## print odd numbers from list

# def is_odd_num(l):
#     enum = []
#     for n in l:
#         if n % 2 != 0:
#             enum.append(n)
#     return enum    
# print(is_odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

############## print first word from string
# def first_word(text: str):
#     return text.split()[0]
# print(first_word("Hello big wide world"))

# ############## verify password
# def is_acceptable_password(password: str) -> bool:
#     if len(password) > 6:
#         return True
#     else: 
#         return False
# print(is_acceptable_password("lolly"))

############## find number of digits in integer
# print(len(str(12)))
# str() function returns the string version of the given object. 
# len() function returns the number of items in an object. 
# So, str(number) converts the variable number to the string, 
# then len() function returns the length of it.

# def end_zero(num: int):
#     n = 0
#     while num%10 == 0:
#         n += 1
#         return n
#     else:
#         return 0
# print(end_zero(300))

s = 100
len(s) = len(s.rstrip('0'))