import csv

# with open("")as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter="-")
#     for line in csv_reader:
#         print(line)

# population = []

# with open("2016_pilbara.csv", mode="r")as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         population.append(line)

# print(population)
# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

# with open("population.csv", mode = "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     for age_group in population:
#         csv_writer.writerow([age_group[0],age_group[1]])

# with open("population.csv", mode="w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     for age_group in population:
#         csv_writer.writerow([age_group[0],age_group[1]])


import csv

# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for donkey in csv_reader:
#         print(f"{donkey[0]} {donkey[1]} {donkey[2]}")

# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for donkey in csv_reader:
#         print(f"{donkey[2]} {donkey[1]} {donkey[0]}")

# parrots = []

# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for donkey in csv_reader:
#         # print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")
#         parrots.append(donkey)
# parrots.pop(0)       
# for donkey in parrots:
#     print(f"{donkey[2]}, Hex: {donkey[1]}, RGB: {donkey[0]}")

# data = []
# count = 0
# with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for line in csv_reader:
#         data.append(line)
# for colour in data: #telling python what we want to do with this variable called colour
#     if "yellow" in colour[2]:
#         # print(colour[2])
#         count = count+1
# print(f"Yellow: {count}")

data = []
count_yellow = 0
count_red = 0
count_green = 0
count_blue = 0
with open("starter\colours_20_simple.csv", mode="r",) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        data.append(line)
for colour in data: #telling python what we want to do with this variable called colour
    if "yellow" in colour[2]:
        # print(colour[2])
        count_yellow = count_yellow+1
    if "red" in colour[2]:
        count_red = count_red+1
    if "green" in colour[2]:
        count_green = count_green+1
    if "blue" in colour[2]:
        count_blue = count_blue+1
print(f"Yellow: {count_yellow}")