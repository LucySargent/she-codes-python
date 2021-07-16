#Loops - repetitive tasks
#Loop - for loops, while loops
#For loops - know how many times to repeat
#while loops - don't know how many times to repeat
#For Loops - sequence, strings, lists, dictionaries

# a = [1,2,3,4]
# print(a[1:4])

# #in this ex we are iterating through a sequence of numbers - our range is a range of integers
# for number in range(10): #number is a variable here - this line is to iterate through a seqeunce of numbers: 0,1,2,3.. 9
#     # runs the indendent elements until the number of times is reached
#     print(number)

# for num in range(5): #default starting point is 0 - is not stated here
#     print(num)

# for num in range(1,11):
#     print(num)

# for num in range(1,11,2):
#     print(num)

#use for loop to print numbers
#0 to 100 (inclusive)
# for num in range(101):
#     print(num)

# use for loop to print numbers
# 0 to 100 (skip 5) 0,5,10,15
# for num in range(0,101,10):
#     print(num)

# letters = ['a','b','c','d']

# for letter in letters:
#     print(letter)


# letters = ['a','b','c','d']
# result = ""
# for letter in letters:
#     result = result + letter
#     print(result) #indented print so printing again and again until the for loop is complete

# letters = ['a','b','c','d']
# result = ""
# for letter in letters: #remember the variable name (here we used letter) is totally arbitary - can be anything you want
#     result = result + letter
# print(result) #printing outside of the 'for loop' so will only print one line

# chilli_wishlist =["igloo","chicken","donut","box"]

# for item in range(len(chilli_wishlist)): #range(4) item -> 0
#     print(chilli_wishlist[item]) #square brackets are extracting list items

# for item in chilli_wishlist:
#     print(item) 

#adapt the for loop to print a message
#for each item in the list e.g. chilli wants: Items"
# for item in chilli_wishlist:
    # print (f"Chilli does not want: {item}")
    
#or print("Chilli wants:", item)
    # print(chilli_wishlist[0])

#use a for loop to print each item in a list from a previous exercise or example

# numbers = [
#     [1,2,3],
#     [4],
#     [5,6]
# ]
# print(numbers[2][-1]) #getting the 6

### NESTED LISTS
numbers = [
    [1,2,3],
    [4],
    [5,6]
]
for number in numbers:
    for digit in number:
        print(digit)

# chilli_wishlist = [
#     ["igloo"],
#     ["donut","tennis", "croc"],
#     ["chicken", "peanut butter"],
#     ["box", "kong", "dig mat"]
# ]
# for category in chilli_wishlist:
#     for item in category:
#         print(item)

######################################
###while loops - repeat number not known

# count = 0
# while count < 5:
#     print("hello")  
#     # count = count + 1 #this code is the same as line below
#     count += 1 #this will output hello five times (after the fourth hello the loop is broken because the condition is no longer met)

    
    

