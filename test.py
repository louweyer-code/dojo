grid = [
    [1, 0, 0],
    [2, 1, 2],
    [2, 1, 0]
    ]

def print_grid():
    for row in grid:
        print(row)


def check_move(start, end):
    if 0 not in grid[end]:
        print('no space')
        return False
    
    if start == end:
        print('same beaker')
        return False
    
    full = len([cell for cell in grid[start] if cell != 0])
    empty = len([cell for cell in grid[end] if cell == 0])
    
    if full > empty:
        print('beaker is full')
        return False
    
    start_number =  None
    end_number = None

    for i in reversed(grid[start]):
        if grid[start][i] != 0:
            start_number = grid[start][i]
            break

    for i in reversed(grid[end]):
        if grid[start][i] != 0:
            end_number = grid[end][i]
            break

    if start_number != end_number:
        print('number doesnt match')
        return False
    
    return True

    # start_cell_top = max([num for num in grid[start] if num != 0])
    # end_cell_top = max([num for num in grid[end] if num != 0])

    # if start_cell_top != end_cell_top:
    #     print('color doesnt match')
    #     return False
    
    return True
    

while True:
    print_grid()
    start = int(input("Which beaker do you want to pour: ") - 1)
    end = int(input("Where do you wanna pour it?: ") - 1)

    if check_move(start, end):
        print('legal move')
        

    else:
        print('invalid move')



    
