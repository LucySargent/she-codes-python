# ### FUNCTIONS
# # syntax

# import csv
# from os import write
# with open("file name inc. type", mode = "r", encoding = "utf-8" as csv file:
# 	csv_reader = csv.reader(csv_file, delimiter=",")  #creates the reader object
#         for line in csv_reader:
#             #print(line)
#             asli_said.append(line)

# print(asli_said)

# with open("asli_says.txt", mode="w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)  #creates the writer object
#     for item in asli_said:
#         csv_writer.writerow(item)

#she saved items in a text doc as a list and then brought the list into a new text file. 
#the new file had extra lines in it. The newline="" parameter handles that. 

### FUNCTIONS
#syntax

# def ask_name(): #we haven't given any perams in the brackets
#     name = input("what's you name? ")
#     return name

# lucy_name = ask_name()
# print(lucy_name)




# # def ask_name(): #we haven't given any perams in the brackets
# #     name = input("what's you name? ")
# #     return name

# # lucy_name = ask_name()
# # print(lucy_name) #use brackets when calling a function

# def create_greeting(name): 
#     greeting = f"Hello {name}"
#     return greeting

# print(create_greeting("Chilli"))  #python is assigning the word here (chilli) to the variable called name. same as saying name = "chilli"

# print(create_greeting("Sara"))

# #Create function that takes in an integer
# #as a parameter and returns that integer
# #multiplied by 3

# def ask_integer():
#     integer = int(input("How old are you?"))
#     return integer
# print(ask_integer()*3)


# def times_3(num): #the brackets show it's a function
#     return num * 3
# print(times_3(5))
# print(times_3(10))
# print(times_3(2)+6)
# print(times_3("hello"))  #we can put any value into the num variable 

# name = Asli #global variable
# def ask_name(): #we haven't given any perams in the brackets
#     name = input("what's you name? ") #local variable
#     name = input("what's you name? ") #local variable
#     return name

# asli_name = ask_name()
# print(asli_name) 
# print(name)


# def convert_cm_to_in(length_cm):
#         length_in_inch = length_cm / 2.54
#         return length_in_inch

# print(convert_cm_to_in(20))

# print(length_in_inch) #is not defined because it's a local variable

#write a function that converts inches to 
#centimeters

# def convert_inch_to_cm(length_in):
#         length_in_cm = length_in * 2.54
#         return length_in_cm #return exits us out of a function
# print(convert_inch_to_cm(10))


# def add(a,b):
#     # result = a + b
#     # return result
#     # print(a + b)
#     return a+b
# print(add(2,3))

# def calculate_mean(a, b):
#     total = a + b
#     mean = total / 2
#     return mean
# print(calculate_mean(3,4))


# def convert_f_to_c(temp_in_f):
#     convert_f_to_c = (temp_in_f - 32) * (5/9)
#     return convert_f_to_c
# print(convert_f_to_c(10))


# def is_it_odd(num):
#     if num % 2 == 0: #modulo - if there is zero remaining the number is not odd so return false
#         return False
#     else:
#         return True
# print(is_it_odd(9))

#see python fizzbuzz

#mean = sum of inputs divided by number of inputs

# def mean(num_list):
#     return sum(num_list) / len(num_list)

# print(mean([4, 3, 2, 6]))

# def total_cost(price,quantity):
#     return price * quantity  #putting $ here will make it a string
# print(f"The total cost is ${total_cost(4.25, 3)}")












