# import csv
# from os import write
# with open("file name inc. type", mode = "r", encoding = "utf-8" as csv file:
# 	csv_reader = csv.reader(csv_file, delimiter=",")  #creates the reader object
#         for line in csv_reader:
#             #print(line)
#             asli_said.append(line)

# print(asli_said)

# with open("asli_says.txt", mode="w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)  #creates the writer object
#     for item in asli_said:
#         csv_writer.writerow(item)

#she saved items in a text doc as a list and then brought the list into a new text file. 
#the new file had extra lines in it. The newline="" parameter handles that. 

### FUNCTIONS
#syntax

def ask_name(): #we haven't given any perams in the brackets
    name = input("what's you name? ")
    return name

lucy_name = ask_name()
print(lucy_name)




