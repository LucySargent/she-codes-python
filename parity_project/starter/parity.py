import csv


def load_grid(csv_file_path):
    """Loads data from a csv file.

    Args:
        csv_file_path: string representing the path to a csv file.
    Returns:
        A list of lists, where each sublist is a line in the csv file.
    """
    grid_list = []
    with open (csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =",")
        for line in csv_reader:
            grid_list.append(line)
        return grid_list


def add_column(grid):
    """Adds a new column to a grid. For each row, if there is an even
    number of X characters, a O is added to the row, otherwise a X is added
    to the row.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new column added.
    """
    """ small_grid,medium_grid,large_grid,empty_grid,all_x """

    for list in grid:
        X_count = 0
        for element in list:
            if element == "X":
                X_count += 1
        if X_count %2 == 0:
            list.append("O")
        else: 
            list.append("X")
    return grid



def add_row(grid):
    """Adds a new row to a grid. For each column, if there is an even
    number of X characters, a O is added to the column, otherwise a X is added
    to the column.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        The same grid, with a new row added.
    """
    new_line = []
    if grid == []:
        return grid
    else:
        for column in range(len(grid[0])): #telling how may times to run the loop
            count_x = 0
            for row in grid:
                if row[column] == "X":
                    count_x += 1
            if count_x % 2 == 0:
                new_line.append('O')
            else:
                new_line.append('X')
    grid.append(new_line)
    return grid


def flip_cell(x_pos, y_pos, grid):
    """Prompts the user to choose a cell to swap from X to O (or vice versa).

    Arguments:
        x_pos: An integer representing the x coordinate of the cell.
        y_pos: An integer representing the y coordinate of the cell.
        grid: A list of lists, where each sublist represents a row in a grid.

        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = x: 0, y: 0
            b = x: 1, y: 0
            c = x: 0, y: 1
            d = x: 1, y: 1

    Returns:
        The same grid, with a cell switched.
    """

    if grid[y_pos][x_pos] == "X":
        grid[y_pos][x_pos] = "O"
    else:
        grid[y_pos][x_pos] = "X"
    return grid


def find_flipped_cell(grid):
    """Determines which cell/cell in the grid was flipped.

    Arguments:
        grid: A list of lists, where each sublist represents a row in a grid.

    Returns:
        A list containing the coordinates of the cell with the flipped cell.
        In the following grid:
            a b
            c d
        These are the coordinates of each letter:
            a = (0, 0)
            b = (1, 0)
            c = (0, 1)
            d = (1, 1)
        If 'a' was the flipped letter, this function would return: [0, 0]
    """
    new_list = []
    for column in range(len(grid)): 
        xcount = 0
        for row in grid: 
            if row[column] == "X": 
                xcount += 1  
        if xcount %2 != 0:     
            new_list.append(column) 
    for x, row in enumerate(grid): 
        xcount2 = 0
        for column in (row): 
            if column == "X":
                xcount2 += 1
        if xcount2 %2 != 0:        
            new_list.append(x)
    return new_list
    
