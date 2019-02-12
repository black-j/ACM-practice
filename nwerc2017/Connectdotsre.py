
import sys
from collections import defaultdict

def greater(right, left):
    if ord(right) >= 97:
        right = right.upper()
    elif ord(right) >= 65 and ord(right) <= 90:
        right = right.lower()
        
    if ord(left) >= 97:
        left = left.upper()
    elif ord(right) >= 65 and ord(left) <= 90:
        left = left.lower()
        
    return right > left

def print_list(to_print):
    for i in to_print:
        for j in i:
            print(j,end = '')
        print()
        
def check_fir_last(to_print,zero_coord, large_coord):
    if zero_coord == large_coord:
        return
    elif zero_coord[0] == large_coord[0]:
        for i in range(min(zero_coord[1], large_coord[1]) + 1,max(zero_coord[1], large_coord[1])):
            if to_print[zero_coord[0]][i] not in ['-','+','.','|']:
                return
        for i in range(min(zero_coord[1], large_coord[1]) + 1,max(zero_coord[1], large_coord[1])):
            to_print[zero_coord[0]][i] = '.'
    elif zero_coord[1] == large_coord[1]:
        for i in range(min(zero_coord[0], large_coord[0]) + 1,max(zero_coord[0], large_coord[0])):
            if to_print[i][zero_coord[1]] not in ['-','+','.','|']:
                return
        for i in range(min(zero_coord[0], large_coord[0]) + 1,max(zero_coord[0], large_coord[0])):
            to_print[i][zero_coord[1]] = '.'
            
def solve(puzzle, row_num, col_num, largest,zero_coord):
    check_fir_last(to_print,zero_coord, large_coord):
    explored = set()
    recur_sol(puzzle,coord_x, coord_y, x_dir, y_dir, expolred)

def recur_sol(puzzle, x, y, x_dir, y_dir, explored):
    if x >= width or x < 0 or y >= height or y <0:
        return 0
    if puzzle[x][y] == '.':
        if x_dir
    if any(recur_sol(map_area,explored,x - 1,y,height, width)
    recur_sol(map_area,explored,x + 1,y,height, width)
    recur_sol(map_area,explored,x,y - 1,height, width)
    recur_sol(map_area,explored,x,y + 1,height, width)):
        if puzzle[x][y] == '-' or puzzle[x][y] == '|':
            puzzle[x][y] = '+'
            return

    a = recur_sol(puzzle, row_num, col_num, largest,zero_coord)
if __name__ == "__main__":

    puzzle = []
    row_num = 0
    col_num = 0
    largest = '.'
    large_coord = 0
    for line in sys.stdin:
        line = line.strip()
        if line != '':
            col_num = len(line)
            for i in range(len(line)):
                if line[i] != '.': 
                    if greater(line[i], largest):
                        largest = line[i]
                        large_coord = (row_num, i)
                    if line[i] == '0':
                        zero_coord = (row_num, i)
            row_num += 1
        else:
            solve(puzzle, row_num, col_num, large_coord,zero_coord)
            print()
            row_num = 0 #reset all settings for next map
            col_num = 0
            largest = '.'
    solve(puzzle, row_num, col_num, large_coord,zero_coord)
            
