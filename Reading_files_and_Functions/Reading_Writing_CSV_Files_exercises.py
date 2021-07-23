import csv

# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for donkey in csv_reader:
# #         print(f"{donkey[0]} {donkey[1]} {donkey[2]}")

# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for donkey in csv_reader:
# #         print(f"{donkey[2]} {donkey[1]} {donkey[0]}")

parrots = []

with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for donkey in csv_reader:
        # print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")
        parrots.append(donkey)
parrots.pop(0)       
for donkey in parrots:
    print(f"English: {donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")

# # data = []
# # count = 0
# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for line in csv_reader:
# #         data.append(line)
# # for colour in data: #telling python what we want to do with this variable called colour
# #     if "yellow" in colour[2]:
# #         # print(colour[2])
# #         count = count+1
# # print(f"Yellow: {count}")

# data = []
# count_yellow = 0
# count_red = 0
# count_green = 0
# count_blue = 0
# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for line in csv_reader:
#         data.append(line)
# for colour in data:
#     if "red" in colour[2]:
#         count_red = count_red +1
# print(f"Red: {count_red}")
# for colour in data:
#     if "green" in colour[2]:
#         count_green = count_green+1
# print(f"Green: {count_green}")
# for colour in data:
#     if "blue" in colour[2]:
#         count_blue = count_blue+1       
# print(f"Blue: {count_blue}")
# for colour in data:
#     if "yellow" in colour[2]:
#         count_yellow = count_yellow+1
# print(f"Yellow: {count_yellow}")


# data = []
# count_yellow = 0
# count_red = 0
# count_green = 0
# count_blue = 0
# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for line in csv_reader:
#         data.append(line)
# for colour in data:
#     if "red" in colour[2]:
#         count_red = count_red +1
#     if "green" in colour[2]:
#         count_green = count_green+1
#     if "blue" in colour[2]:
#         count_blue = count_blue+1       
#     if "yellow" in colour[2]:
#         count_yellow = count_yellow+1
# print(f"Red: {count_red}")
# print(f"Green: {count_green}")
# print(f"Yellow: {count_yellow}")
# print(f"Blue: {count_blue}")


#5.galaxies.py contains 82 different galaxies and their velocities(km/sec). 
# output the galaxy with the slowest velocity
# output the galaxy with the highest velocity

# space_data = []
# import csv

# with open("starter\galaxies.csv", mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for line in csv_reader:
#         space_data.append(line)

# def min_velocity(velocity):
#     min_velocity = 
#     print(min(space_data,))
# def max_velocity(velocity):


# In this program, the slow / fast variables allow us to compare the velocity values with the variable values (inf and 0).
# The loop iterates over every row. We use the slow / fast variables to find the first slowest and fastest values. 
# The loop updates the slow / fast variables with the lastest values identified.  

# import csv 
# with open("starter\galaxies.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     slow = [None, float('inf')] #ignores first. Variable value = infinity (huge) 
#     fast = [None, 0] #ignores first. Variable value = 0 (low)
#     for i, row in enumerate(csv_reader): #i means index (naming convention). Row is row.
#         if i != 0: #this first 'if' in the loop ensures each value is checked when the loop iterates because no rows = 0.
#             if int(row[1]) < slow[1]: #this 'if' (within the first'if') targets velocity data in each row: e.g. row[1] for row (18,19349) gets (19349). If velocity value is less than current slow value, do this: 
#                 slow =  [row[0], int(row[1])] #this line re-defines the slow var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be lower than the last one stored)
#             if int(row[1])> fast[1]:#this 'if' (within the first'if') says if velocity is greater than current fast value, do this:
#                 fast = [row[0], int(row[1])] #this line re-defines the fast var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be faster than the last one stored)

#     print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.') #formatted print returns the new slow variable - galaxy + value
#     print(f'Galaxy {fast[0]} has a max velocity of {fast[1]}km/sec.') #formatted print returns the new fast variable - galaxy + value