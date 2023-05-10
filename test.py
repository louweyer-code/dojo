grid = [
    [1, 0, 0],
    [2, 1, 2],
    [2, 1, 0]
    ]

# beaks = [['-','-','-'],
#          [1, 2, 3]]

def print_grid():
    for row in grid:
        print(row)

# def print_legend():
#     spacer = ['-', '-', '-']
#     column = [1, 2, 3]
#     print(' '.join(map(str, spacer)))
#     print(' '.join(map(str, column)))

def check_move(start, end):
    if 0 not in grid[end]:
        print('no space')
        return False
    
    if start == end:
        print('same beaker')
        return False
    
    start_cell_top = max([num for num in grid[start] if num != 0])
    end_cell_top = max([num for num in grid[end] if num != 0])
    if start_cell_top != end_cell_top:
        print('color doesnt match')
        return False
    
    return True
    

#for row in grid:
    #print(row)

while True:
    print_grid()
    start = int(input("Which beaker do you want to pour: ") - 1)
    end = int(input("Where do you wanna pour it?: ") - 1)

    if check_move(start, end):
        print('legal move')

    else:
        print('invalid move')



    
