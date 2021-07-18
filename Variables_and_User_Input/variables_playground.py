# #variables
# #strings - use " " or ' ' - either quote type is ok but be consistent
# dog = "Gigi"
# print (dog)
# print(type(dog))
# Lucy = f"Hey, my dog's name is {dog}!"
# print(Lucy)
# day = "Saturday"
# message = f"Today is {day}"
# print(message)
# print(type(day))
# month = "July"
# message2 = f"The month is {month}"
# print(message2)
# print(type(month))
# Dinner = "Mexican"
# message3 = f"Tonight we're having {Dinner} for dinner"
# print(message3)
# print(type(Dinner))

#Integer, float
apples = 5
banana = 8
fruits = apples + banana
# print(fruits)
# print(type(fruits))

# height = 5.1
# weight = 10.1
# calculation = weight - height
# print(calculation)
# print(type(calculation))
# calculation = height + banana
# print(calculation)

# #Integers
# #Run distance in m
# run1_dist = 1000
# run2_dist = 3000

# #Addition
# total_distance = run1_dist + run2_dist
# print(total_distance) 

# #Floats
# #Run distance in km
# run3_dist = 1.7
# run4_dist = 1.35

# #Addition
# #Division is always a float
# total_distance = run3_dist + run4_dist
# print(total_distance) 

# #Division
# example_distance = run1_dist / run2_dist
# print(example_distance) 

# #Division and mult
# example_distance = run1_dist / 1000
# print(example_distance) 
# print(run1_dist / 1000)
# print(run3_dist * 1000)

# goal_dist = 5000
# run2_left = goal_dist - run2_dist
# print(run2_left)


var1 = "banana"
var2 = 5
var3 = "3"
var4 = 10

#str + int - we are typecasting here - converting int to str
# print(var1 + str(var2))

# use int as a str - var 3 has double quotes, making it a string
# print(var2 + int(var3))

#multiply str by int
# print(var1 * var2)

# #int to float
# print(float(var2))

# #answers to divisions are floats
# calculation = var4 / var2
# print(calculation)

# run5_dist = "5000"
# # print(run5_dist + 3) #error - can only concatenate str (not "int") to string
# print(run5_dist + "3") #5003 - ok to add str + str
# print(run5_dist * 3) #500050005000 -  repeating the str by the integer value
# print(run5_dist * 3.0) #error - can't multiply sequence by non-int of type 'float'

# run5_dist = "5000"
# print(run5_dist + 5) #error - can only concatenate str (not "int") to string
# print(run5_dist + str(5)) #typecasting from int to str
# print(run5_dist + "5") #using int as str
# print(run5_dist + 5.5) #error - can only concatenate str (not "float") to str
# print(run5_dist + str(5.5)) #typecasting from float to str
# print(run5_dist * 2) #repeats the str by the integer value
# print(run5_dist * "2") #error can't multiply sequence by non-int of type 'str'
run5_dist = 50
calculation= run5_dist * 2
print (calculation)