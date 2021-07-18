# 1. Kate’s cat,Roary,loves catching moths.
# # Write a program that determines whether or not it is time for Roary to catch moths.

# moths_in_house = True
# mitch_is_home = True

# if moths_in_house:
#     print("Get the moths!")
# if not moths_in_house:
#     print("No threats detected.") 

#################################

# 2. Roary can’t get the moths by herself! 
# Amend the previous program to determine whether or not it's time for Roary to go hunting

# if moths_in_house and mitch_is_home:
#     print("Hooman! Help me get the moths!")
# if not moths_in_house and not mitch_is_home:
#     print("No threats detected.") 
# if moths_in_house and not mitch_is_home:
#     print("Meoooooooooow! Hisssssss!")
# if not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")

###########################

#3. Write a program that implements the algorithm for red light Cameras 

# light_colour = "Red"
# car_detected = True

# if light_colour == "Red" and not car_detected:
#     print("Do nothing.")
# elif light_colour == "Red" and car_detected:
#     print("Flash!")
# elif light_colour == "Green" and not car_detected:
#     print("Do nothing.")
# elif light_colour == "Green" and car_detected:
#     print("Do nothing.")
# elif light_colour == "Amber" and not car_detected:
#     print("Do nothing.")
# elif light_colour == "Amber" and car_detected:
#     print("Do nothing.")

#V2
# if light_colour == "Red" and car_detected:
#     print("Flash!")
# else:
#     # print("Do nothing.")

###############################

#4. Write a program that asks user for their height,
# and determines whether or not they are tall enough to ride the rollercoaster, 
# which has a height requirement of 120cms.

# height = input("How tall are you in cms? ")
# requirement = 120
# if float(height) >= int(requirement):
#     print("Hop on!")
# else:
#     print("Sorry, not today :(")

################################

#5. Write a program that asks the user to enter their username and password,
# and outputs a success message if they are correct, 
# or a failure message if they are incorrect

# username = "fleur"
# password = "password123"
# entered_username = input("Username: " )
# entered_password = input("Password: " )
# if entered_username == username and entered_password == password:
#     print("Correct!")
# else:
#     print("Incorrect!")

##################################

#6.Write a program that asks the user to enter their email address
# and checks whether it is valid or not.
# For the purpose of this exercise,you can make the assumption 
# that a valid email address contains a “@” symbol and a “.” symbol 

# email = input("Enter your email address: ")
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
    