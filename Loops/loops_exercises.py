#Q1. Ask the user for a number. 
#Use a for loop to print the times tables for that number.

# number = int(input("Enter a number: "))
# for i in range(1,number +1):
#     print(f"{number} * {i} = ", int(number) *int(i))

#########################################

#Q2. Ask the user for a number. 
#Use a for loop to sum from 0 to that number.

# value = int(input("Enter a number: "))
# sum = 0
# for value in range(value+1):
#     sum = sum + value
# print(sum)

#######################################

#Q3. Given a list, use a for loop to sum all the numbers in the list. 

total = 0
list = [3, 5, 9, 1]
for ele in range(0, len(list)):
    total = total +list[ele]
print("Total:", total)

# total = 0
# list = [-3, -5, 9, 1]
# for ele in range(0, len(list)):
#     total = total +list[ele]
# print("Total:", total)

# total = 0
# list = []
# for ele in range(0, len(list)):
#     total = total +list[ele]
# print("Total:", total)

##############################################

#Q4. Use a for loop to format and print the following list

# mailing_list = [
#     ["Chilli", "chilli@thechihuahua.com"],
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Ivy", "noreply@goldendreamers.xyz"],
# ]
# for item, item in mailing_list:  
#     print(f"{item}: {item}")