### EXAMPLES

# guess = ""
# while guess != "a":
#     guess = input("Guess a letter: ")

# counter = 10
# while counter <= 10:
#     print(counter)
#     # counter = counter + 1 #this line stops it being an infinite loop

##############################

# EXERCISES
# 1. Ask user to continuously enter a name until a blank string is entered.

# guess = "a"
# while guess != "":
#     guess = input("Name: ")

# can also do a definition using length:
# check = input("Add a name: ")
# while len(check)>0:
#     check = input("Add a name: ")

# 2. Set a password. Ask user to continually enter a password until they enter the correct password.

# password = input("Enter password: ")
# while password != "password":
#     password = input("Enter password: ")
# if password == "password":
#     print("Correct password!")
# else:
#     print("Incorrect password.")


##############################

#Q1. Continuously ask user to enter a number until they provide a blank input. Output the sum of all the numbers.

# user_number = input("Enter a number: ")
# total = 0
# while user_number != "":
#     total = total + int(user_number)
#     user_number = input("Enter a number: ")
# print(total)


#     Sum = total + int(n)
# print(Sum)

##############################

#Q2. Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).

# n = int(input("Enter a number: "))
# i = 1
# while i<=n:
#     print(i)
#     i=i+2

# # variation - print the even numbers
# n = int(input("Enter a number: "))
# i = 0
# while i<=n:
#     print(i)
#     i=i+2

##############################
# Q3. 
# Select a number. 
# Ask user to enter a number.
# Output whether user number is less than or greater than my number.
# Repeat process unril user guesses correct number.

### V1 - does not recognise if number is too high/low
# num = int(10)
# guess = None
# while guess != num:
#     guess = (input("Guess my number: "))
#     guess = int(guess)

#     if guess == num:
#         print("Correct!")
#         break
#     else:
#         print("Try again")

### V2
# num = int(10)
# guess = None
# while guess != num:
#     guess = (input("Guess my number: "))
#     guess = int(guess)

#     if guess == num:
#         print("Correct!")
#         break
#     if guess < num:
#         print("Too low!")
#     if guess > num:
#          print("Too high!")



#### PLAY
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Loop done.')


# sample_list = ['cat', 'dog', 'bunny', 'pig']
# print("Your list of animals are: {}, {}, {} and {}".format(*sample_list))

############# LOOPS: Exercises extension

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
expenditure = [] #create a blank list for amount spent
for element in groceries:
    value = int(input("How many units of " + element[0] + " did you buy?"))* element[1] #gets the number of items bought as a variable
    expenditure.append([element[0], value])
print("====Izzy's Food Emporium====")
total = 0
for element in expenditure:
    print(str(element[0]) + "\t" + str(element[1]))
    total = total + element[1]   
print("============================")
print(total)






