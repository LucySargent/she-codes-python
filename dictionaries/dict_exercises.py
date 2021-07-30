groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Bacon": 9.00,"Carrots": 0.56,"Oranges": 3.08
}
quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

#groceries - using as main dict. key is relevant to both dicts. 
# for key,value in groceries.items():
#     print(f"{quantity[key]} {key} @ ${value} = ${round(quantity[key]*value, 2)}")

#quantity = {"Baby Spinach": 2,"Hot Chocolate": 1,"Crackers": 4,"Bacon": 0,"Carrots": 8,"Oranges": 5}

#look at one item
# print(groceries["spinach"])

#add an item
# groceries["Avocado"] = 1.00
# print(groceries)

# print(groceries["Oranges"]) #prints the value of "Oranges" - 3.08
# print(groceries.keys()) #prints the keys only
# print(groceries.values()) #prints the values only
# print(groceries.items()) #keys and values together

# #remove item
# del groceries["bacon"]
# print(groceries)

#iterating over dict
# for item in groceries:  #"item" is just a variable name, it can be any word (it is not a key python word)
    # print(f"{item}: ${groceries[item]}")  #using formatting to make it look nice!

#another way to iterate over the dict
# for key,value in groceries.items():
    # print(f"{key}: ${value}") #using formatting to make it look nice!

# for key,value in groceries.items():
    # print(key,value) #same as aboe but without the formatting.

colour_counts = {  #dictionary
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

#Iterate over the colours list.Track number of times colour occurs in list - update counter in dictionary

# colours = [  #list
#     "purple", #first item passed in loop
#     "red", #second item passed in loop
#     "yellow",
#     "blue",
#     "purple",
#     "orange",
#     "blue",
#     "purple",
#     "orange",
#     "green"
# ]

# colours = ["orange","purple","blue","yellow","green","green","purple","purple","green","blue","green","orange","purple","blue","green","orange","orange","red","yellow","yellow"]

# for colour in colours:
#     colour_counts[colour] += 1  #updating the count
# for colour in colour_counts:
#     print(f"{colour}: {colour_counts[colour]}")

# names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy","Joy", "Katie", "Maddie", "Tash", "Nic","Rachael", "Bec", "Bec", "Tabitha", "Teagen","Viv", "Anna", "Catherine", "Catherine", "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy","Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

#create empty dictionary
#for each name in the list, append to dictionary
# new_dictionary = {}
# for name in names:
#     new_dictionary[name] = 0 #creating the key:value in the dictionary
# for name in names:
#     new_dictionary[name] += 1 #counting number of times 
# for name in new_dictionary:
#     print(f"{name} {new_dictionary[name]}") #output

#Read the colour data from colours_20_simple.csv and save the data in a dictionary
#the key is the hex code, the value is the English name e.g. #BEBD7F: Green beige 

##### this one only prints the values  ######
# import csv
# with open("colours_20_simple.csv", "r")as lucy:
#     csv_reader = csv.reader(lucy, delimiter=",")
#     next(csv_reader)
#     colours_dict = {}
#     for line in csv_reader:
#         colours_dict[line[1]] = line[2]
#     for line in colours_dict:
#         print(f"{colours_dict[line]}")

##### this one prints items #####
import csv
with open("colours_20_simple.csv", "r")as myfile:
    csv_reader = csv.reader(myfile, delimiter=",")
    next(csv_reader)
    colours_dict = {}
    for line in csv_reader:
        colours_dict[line[1]] = line[2]
        # print(f"{line[1]}:{colours_dict[line[1]]}")
    for key, value in colours_dict.items():
        print(f"{key}: {value}")    


