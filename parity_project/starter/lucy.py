grid = [
  ["X","O","X","O"],
  ["X","X","W","X"],
  ["X","A","X","O"],  # [1][2] col/row
  ["X","X","O","O"],
]
# Returns: A list containing the coordinates of the cell with the flipped cell.
# return index like this ([1,2])

# print(grid[1][2]) # W
# print(grid[2][1]) # A- this is the one I want.
#COORDINATES ARE NOT THE SAME AS THE INDEX
#the index is grid[2][1] (row,col) but the coordinates are 1,2 (col,row)
grid = [
  ["X","O","X","O"],
  ["X","X","O","O"],
  ["X","X","X","O"],    # index [2][1] (row/col) but coordinates ([1,2]) (col/row)
  ["X","X","O","O"],
]
new_list = []
for column in range(len(grid)): #sets up the loop to go through the list as many times as the list is long i.e. number of columns - which makes column a number
    xcount = 0
    for row in grid: #sets up to go through each row
        if row[column] == "X": # remember column is a number
            xcount += 1 # calculate xcount at the end of each column. Then loops back to line 23
    # print(xcount2) 
    if xcount %2 != 0:  #finds the odd x count     
        new_list.append(column) #appends the column number to the list
for x, row in enumerate(grid): #sets up to loop through whole row. x is getting the number of the row so x is a number
    # print(x)
    xcount2 = 0
    for column in (row): #for each element in the row that I am looking at at the moment (one row at a time starting with line 15)
        if column == "X":
            xcount2 += 1
    if xcount2 %2 != 0:        
        new_list.append(x)
print(new_list)

    

# grid = [
#   ["A","X","C","X"],
#   ["A","X","C","X"],
#   ["A","X","C","X"],   
#   ["A","X","C","X"],
# ]








# print(grid[2][1]) #returns W

# new_list = []
# for column in range(len(grid)): #range being length w/e
#     countx = 0
# for row in grid:
#     if row[column] == "X":
#         countx += 1
#     print(countx)
        # if countx %2 != 0:
        #     print(f"{column}")




# grid = [
#     ["a","b","c"],
#     ["d","e","f"],
#     ["g","h","i"],
# ]
# print(grid[0][1])
# for i in (grid):
#     for element in (i):
#         print(element)

#how to turn the user input 0,1 (d) into the list index

# line = int(input(f"ROWS going down from 0. Choose a number between 0 and {len(grid)}: ")) 
# column = int(input(f"COLUMNS going across from 0. Choose a number between 0 and {len(grid[0])}: "))
# # flip_cell = [line][column]
# if grid[line][column] == "X":
#     grid[line][column] = "O"
# else:
#     grid[line][column] = "X"
# print(grid)


# def flip_cell(0, 1, grid):


# cellx = f"[{x_axis}]"
# cellr = f"[{y_axis}]"
# final_cell = cellx + cellr
# flip_cell = f"grid{final_cell}"
# print(flip_cell)
# if flip_cell == "X":
#     flip_cell = "Y"
# else:
#     flip_cell = "O"

# print (final_cell)
# chilli_wishlist[0] = "carrot" 



# #count the number of X in the column - use index
# #if X is even, add O
# # grid[row][column]
# # i = 0 for row in grid -> [i][0] -> i += 1

# # for index, row in enumerate(my_grid):
# #     print(row[0])

# #if row is blank we need to do soemthing else
# new_line = []
# if grid = []
#     return
# else:
# for column in range(len(grid[0])): #this sets up the number of times to run the loop because the grid has  length of 3
#     count_x = 0
#     for row in grid:
#         if row[column] == "x":
#             count_x += 1
#     if count_x % 2 == 0:
#         new_line.append('0')
#     else:
#         new_line.append('x')
# grid.append(new_line)
# return grid

        # index += 1
        # print(x_count)
    


 #         i += 1
# print(i)
# print(my_grid)

    







# X_count = 0
# for list in my_grid:
#     for element in list:
#         if element == "X":
#             X_count += 1
#     if X_count %2 == 0:
#         list.append("O")
#     else: 
#         list.append("X")
# print(my_grid)


# X_count = 0
# for i, val in enumerate(my_grid):
#     print (i,val)
# for val in my_grid:
#     if val == "X":
#         X_count += 1
# print(X_count)
# if X_count %2 == 0:
#     my_grid += ["New O!"]
# else: 
#     my_grid += ["New X"]
# print(my_grid)


# X_count = 0
# for list in my_grid:
#     for element in list:
#         if element == "X":
#             X_count += 1
#     if X_count %2 == 0:
#         list.append("O")
#     else: 
#         list.append("X")
# print(my_grid)


