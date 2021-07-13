# moths_in_house = True
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print("Hooman! Help me get the moths!")
# if not moths_in_house and not mitch_is_home:
#     print("No threats detected.") 
# if moths_in_house and not mitch_is_home:
#     print("Meoooooooooow! Hisssssss!")
# if not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")

light_colour = "Red"
car_detected = True

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

# if light_colour == "Red" and car_detected:
#     print("Flash!")
# else:
#     # print("Do nothing.")

# height = input("How tall are you in cms? ")
# requirement = 120
# if float(height) >= int(requirement):
#     print("Hop on!")
# else:
#     print("Sorry, not today :(")

# username = "fleur"
# password = "password123"
# entered_username = input("Username: " )
# entered_password = input("Password: " )
# if entered_username == username and entered_password == password:
#     print("Correct!")
# else:
#     print("Incorrect!")

email = input("Enter your email address: ")
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
    