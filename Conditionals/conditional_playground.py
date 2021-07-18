# is_sunny = False #booleans capital
# have_shoes = True
# is_gym_open = True

# print(is_sunny and have_shoes) # and operator. The output is only true if all conditions are true. In this case it returns false because is sunny is false.
# print(is_sunny or is_gym_open) #returns True because at least one is true
# print(not is_sunny) # not operator - swaps the boolean value

# is_raining = False
# is_cold = True
# print(is_raining)
# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)

# is_raining = False
# is_cold = True
# print(is_raining) #F 
# print(not is_raining) #T
# print(is_raining or is_cold) #T because at least one thing (is cold) is true
# print(is_raining and not is_cold) #F because both are now false
# print(is_raining or not is_cold ) #F both are false
# print(not is_raining and not is_cold) #F 

# is_sunny = False #booleans capital
# have_shoes = True
# is_gym_open = True

# print(5 < 3) #we expect this to be false
# print(5 > 3) #we expect this to be true
# print(10 >= 10) #true
# print(4 <= 10) #true
# print(5 == 5) #checking if the valus are the same true
# print(5 != 4) #checking if the values are not equal - true
# print(5.1 > 2.4) #true
# print("Alsi" == "asli") #false
# print("Alsi" != "asli") #true

# temperature = 16
# print(temperature < 18) 
# print(temperature > 20)
# wind_chill = 3
# print(wind_chill > 4)
# print(temperature - wind_chill < 16)
# name = "Charlie"
# print(name == "Hayley")
# print(name != "Hayley")

# print("A" > "A")
# print(ord("A") == 65)
# print (ord("Z"))


#syntax / semantics (the grammar)
# if statement
# var1 = 5
# if var1 < 3:
#     print("hello")  #if this is true then do this
# else:
#     print("goodbye")

# name = "Sara"
# if name == "Lucy":
#     print("Hi, Lucy")
# elif name == "Randall":
#     print("Hi, Randall")
# else:
#     print("Hello")

### IF
is_raining = True
# if is_raining:
#     print("Take umbrella!")

### IF, ELSE
# if is_raining:
#     print("Take an umbrella!")
# else:
#     print("Do not take an umbrella!")

### IF, ELIF, ELSE
# temperature = 34
# wind_chill = 3
# is_raining = False
# if temperature - wind_chill < 16:
#     print("Take jumper!")
# elif temperature - wind_chill > 30: #elif only happens if thing before it is not true
#     print("Euck! It's hot today, stay home.")
# else: 
#     print("Wow, what a lovely day!")

### NESTED IF
temperature = 16
wind_chill = 3
is_raining = False

if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else: 
    if is_raining:
        print("You will need an umbrella today.") 
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.") 


### LISTS
# letters = ["a", "b", "c", "d"] #elements
# # print(letters[-1]) #-1 will always give last value in a list
# # print(letters[-2])#-2 will always give second last value in a list
# print(letters[0:2]) 

# is_raining = True
# is_cold = True
# # print(type(is_raining))
# # print(type(is_cold))

# # print(is_raining)
# # print(is_cold)
# # print(is_raining and is_cold)
# # print(is_raining or is_cold)
# # print(is_raining and not is_cold)
# # print(not is_raining and is_cold)

# print(is_raining) #T
# print(not is_raining) #F
# print(is_raining or is_cold) #T
# print(is_raining and not is_cold) #F
# print(is_raining or not is_cold) #T
# print(not is_raining and not is_cold) #F