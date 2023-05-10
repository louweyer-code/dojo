grid = [
    [0, 2, 0],
    [0, 1, 1],
    [1, 2, 2]
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
        return False
    
    if start == end:
        return False
    
    start_cell_top = max([num for num in grid[start]])
    end_cell_top = max([num for num in grid[end]])
    if start_cell_top != end_cell_top:
        return False
    

#for row in grid:
    #print(row)

while True:
    print_grid()
    start = int(input("Which beaker do you want to pour: "))
    end = int(input("Where do you wanna pour it?: "))

    if check_move(start, end):
        print('legal move')
    else:
        print('invalid move')


#print_legend()




    
