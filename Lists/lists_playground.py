chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# print(chilli_wishlist)
# print(len(chilli_wishlist))

# ## INDEXING

# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[2])
# # print(chilli_wishlist[3])
# print(chilli_wishlist[-1])
# # print(chilli_wishlist[-2])
# # print(chilli_wishlist[-3])
# print(chilli_wishlist[-0])
# # print(chilli_wishlist[0:1])
# # print(chilli_wishlist[0:2])
# print(chilli_wishlist[0:3])
# # print(chilli_wishlist[0:4])
# # print(chilli_wishlist[1:3])
# # print(chilli_wishlist[2:4])

### CHANGING ITEMS IN THE LIST - indicate the item position
# chilli_wishlist[0] = "carrot" 
# chilli_wishlist[1] = "duck"
# print(chilli_wishlist)

### ADDING / REMOVING ITEMS
### Append - adds to end of list
# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# chilli_wishlist.append("dig mat")
# print(chilli_wishlist)

# ### Extend - adds multiple items to the list
# chilli_wishlist.extend(['kong','ball','crocodile'])
# print(chilli_wishlist)

### Insert
# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# chilli_wishlist.insert(1, 'peanuts')
# print(chilli_wishlist)

# ### Pop - remove an item
# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# chilli_wishlist.pop(0)
# # chilli_wishlist.pop(1)
# # chilli_wishlist.pop(2)
# # chilli_wishlist.pop(3)
# # chilli_wishlist.pop("0 igloo") #!!! DOES NOT TAKE A STRING
# print(chilli_wishlist)

### Remove
# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# chilli_wishlist.remove('0 igloo')
# chilli_wishlist.remove('0') #!!! DOES NOT WORK - NOT IN LIST
# print(chilli_wishlist)

# Challenges
# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# add new item to position 2
# chilli_wishlist.insert(2, 'mouse')

# add new item to position 2
# chilli_wishlist.pop(3)

# add four new items to end of list
# chilli_wishlist.extend(['clam','lobster','crab','whale'])

# remove igloo from list
# chilli_wishlist.pop(0)
# print(chilli_wishlist)

### LOGIC WITH LISTS

# chilli_wishlist = ["0 igloo", "1 chicken", "2 donut", "3 box"]
# chilli_wishlist.extend(['clam','lobster','crab','whale','shark'])
# print(chilli_wishlist)
# len(chilli_wishlist)
# print(len(chilli_wishlist))

# if '0 igloo' in chilli_wishlist:
    # print('Chilli would like the igloo.')
# else:
    # print('Chilli does not want the igloo.')

# if len(chilli_wishlist) > 8:
#     print('Chilli wants a lot of stuff!')
# else: 
#     print('Chilli thinks his list is big enough.')

# chilli_wishlist = ["igloo", "chicken", "donut", "box"]
# if not 'blueberries' in chilli_wishlist:
#     print('no blueberries')
#     chilli_wishlist.append('blueberries')
# print(chilli_wishlist)

# ### SUBLISTS
# chilli_wishlist = [
#     ['igloo'], #bed
#     ['donut', 'ball', 'crocodile'], #toys
#     ['chicken', 'peanut butter'], #food
#     ['walk', 'swim', 'chase'] #activities
# ]
# print(len(chilli_wishlist))

# print(chilli_wishlist)
# print(chilli_wishlist[0])
# print(chilli_wishlist[1])
# print(chilli_wishlist[2][1])

### challenges
# change the third item in the second list
# chilli_wishlist[1][2] = 'elephant'
# print(chilli_wishlist[1])

### add another item to the 3rd food sublist
# chilli_wishlist[2].insert(0,'BONE')
# print(chilli_wishlist[2])

# ### add another sublist to the list: sit, lie down, stay
# chilli_wishlist.extend([['sit', 'lie down', 'stay']])
# # print(chilli_wishlist)
# print(chilli_wishlist[4])