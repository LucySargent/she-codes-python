# import csv

# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for donkey in csv_reader:
# #         print(f"{donkey[0]} {donkey[1]} {donkey[2]}")

# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for donkey in csv_reader:
# #         print(f"{donkey[2]} {donkey[1]} {donkey[0]}")

# # parrots = []

# # with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     for donkey in csv_reader:
# #         # print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")
# #         parrots.append(donkey)
# # parrots.pop(0)       
# # for donkey in parrots:
# #     print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")

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

#5.galaxies.py contains data about 82 different galaxies and their velocities (km/sec). 
# Using this data, output the galaxy with the slowest velocity, 
# and the galaxy with the highest velocity

space_data = []
import csv
from typing import SupportsBytes
with open("starter\galaxies.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        space_data.append(line)

def min_velocity(velocity):
    min_velocity = 
def max_velocity(velocity):

