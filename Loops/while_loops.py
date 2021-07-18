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


# # user_number = (input("Enter a number: "))
# # total = 0
# # # user_number = int(user_number)
# # Sum = total + int(user_number)
# # while user_number != "":
# #     Sum = total + int(user_number)
# #     user_number = (input("Enter a number: "))
# #     # user_number = int(user_number)
# # print(Sum)

# ##############################

# #Q2. Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).

# n = int(input("Enter a number: "))
# i = 1
# while i<=n:
#     print(i)
#     i=i+2

# # variation - print the even numbers
# n = int(input("Enter a number: "))
# i = 0
# while i<=n:
# #     print(i)
# #     i=i+2

# ##############################
# # Q3. 
# # Select a number. 
# # Ask user to enter a number.
# # Output whether user number is less than or greater than my number.
# # Repeat process until user guesses correct number.

# ### V1 - does not recognise if number is too high/low
# # num = int(10)
# # guess = None
# # while guess != num:
# #     guess = (input("Guess my number: "))
# #     guess = int(guess)

# #     if guess == num:
# #         print("Correct!")
# #         break
# #     else:
# #         print("Try again")

# ### V2
# num = (10)
# guess = None
# while guess != num:
#     guess = int(input("Guess my number: "))
#     # guess = int(guess)

#     if guess == num:
#         print("Correct!")
#         break
#     elif guess < num:
#         print("Too low!")
#     # if guess > num:
#     #      print("Too high!")
#     else:
#         print("Too high!")


# sample_list = ['cat', 'dog', 'bunny', 'pig']
# print("Your list of animals are: {}, {}, {} and {}".format(*sample_list))

# ############# LOOPS: Exercises extension

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# expenditure = [] #create a blank list for amount spent
# for element in groceries: #iterating over the list - targeting elements by their position in the list
#     value = int(input("How many units of " + element[0] + " did you buy? "))* element[1] #- identifying an element by it's position. Multiply number of units by item cost
#     expenditure.append([element[0], value]) #adds the value in value variable (with calculation) to the list WHY DO WE NEED ELEMENT[0] here?
# print("") 
# print(expenditure)   
# print("====Izzy's Food Emporium====")
# total = 0
# for newlist in expenditure: #loop to iterate over the expenditure list and print it out - loop finishes when last element is listed 
#     print(str(newlist[0]) + "\t" + str(newlist[1])) #printing reciept, trying tab to space elements getting element from ezpenditure list
#     total = total + newlist[1]   #calculating total to pay
# print("============================")
# print(total)
# print("")


print(f"{item[0]:<20} $  {item[1]:.2f}")
print(f"{'$':>22} {total:.2f}")

#confused by use of element word in both lists!

# is there a better way to print this reciept? using the f string thing?

# how does it know that x is a thing in the list? e.g. can x be anything at all?
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# How can I use item / element? (see loops exercises - we use both are they like built in variables?)
# in extension q2, do I need to create a new list for the string?
# what is a tuple?

#Q2. Ask the user to enter a string. Output the string one character at a time, as well as it’s position in the string

# string = input("Please enter a string: ")
# count = 0
# for letter in string:
#     # count = count+1
#     print(f"{count} {letter}")
#     count = count+1

#Q3.Ask the user to enter a string. Output the stringone character at a time, as well as it’s positionin the string

#https://www.programiz.com/python-programming/examples/pyramid-patterns 

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")

digits = [1,2,3,4]
result = 0
for d in digits:
    result = result + d
    print(result)






