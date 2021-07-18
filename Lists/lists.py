#### Lists
# letters = ["a", "b", "c", "d", "e"] #elements
# print(letters[-1]) #-1 will always give last value in a list
# print(letters[-2])#-2 will always give second last value in a list
# print(letters[0:2])
# print(letters)
# print(letters[0:3:2]) #skip one - so output is a, c
# print(letters[1:5:3]) 
# print(letters[1:4:3])
# print(letters[1:4]) 

# chilli_wishlist = ["0igloo", "1chicken", "2donut toy","3cardboard box"]

# INDEXING
# print(len(chilli_wishlist)) #len showing the number of items in a container
# print(chilli_wishlist)
# print(type(chilli_wishlist))
# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[-1])

###SLICING
# print(chilli_wishlist[0:2]) #does not print the second index it stops at 2
# print(chilli_wishlist[1:3])
# chilli_wishlist[-2] = "carrot"
# print(chilli_wishlist)

# chilli_wishlist = ["0igloo", "1chicken", "2donut toy","3cardboard box"]
#print sublist of items in positions 2 through 3 [2] and [3]
# print(chilli_wishlist[2:4])

#print the item in -3 (chicken)
# print(chilli_wishlist[-3])

#change value of  first item in list
# chilli_wishlist[0] = "banana"
# print(chilli_wishlist[0])

#APPEND / EXTEND (use extend to add several values)
# letters = ["a", "b", "c", "d", "e"]
# letters.append("f")
# print(letters)
# print(letters.extend(["g","m"]))
# print(letters)
# print(letters)

#INSERT 
# letters.insert(1, "z")
# print(letters)

#POP - removing a value from a list
# a = letters.pop(2)

#REMOVE - uses a str
# letters.remove("d")
# print(letters)

chilli_wishlist = ["0igloo", "1chicken", "2donut toy","3cardboard box"]

# chilli_wishlist.append("dig mat")
# chilli_wishlist.extend(["Kong", "tennis ball", "crocodile"])
# chilli_wishlist.pop() #default is the last item
# chilli_wishlist.pop(2)
# print(chilli_wishlist)

if "tennis ball" in chilli_wishlist:
    print("chilli would like a ball")
else:
    print("chilli doesn't want to play")
if len(chilli_wishlist > 8):
    print("chilli wants stuff")

# #A NESTED LIST
# chilli_wishlist = [
#     ["igloo"],
#     ["donut toy", "tennis", "croc"]
#     ["chicken", "butter"]
#     ["box"],
# ]
# print(chilli_wishlist[2])

