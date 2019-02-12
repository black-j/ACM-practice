
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
            
def solve(dot_dict, ver_dict, row_num, col_num, largest,zero_coord):
    to_print = []
    to_dash = False
    #print -
    for row in range(row_num):
        to_print.append([])
        for col in range(col_num):
            if row in dot_dict and col in dot_dict[row]:
                to_print[row].append(dot_dict[row][col])
                del dot_dict[row][col]
                if len(dot_dict[row]) > 0:
                    to_dash = True
                else:
                    to_dash = False
            elif to_dash:
                to_print[row].append("-")
            else:
                to_print[row].append(".")
    #print |
    to_dash = False
    for col in range(col_num):
        for row in range(row_num):
            if col in ver_dict and row in ver_dict[col]:
                del ver_dict[col][row]
                if len(ver_dict[col]) > 0:
                    to_dash = True
                else:
                    to_dash = False
            elif to_dash and to_print[row][col] == '-':
                to_print[row][col] = "+"
            elif to_dash:
                to_print[row][col] = "|"
    check_fir_last(to_print,zero_coord, largest)
    print_list(to_print)

if __name__ == "__main__":

    dot_dict = defaultdict(dict)
    ver_dict = defaultdict(dict)
    connected = dict()
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
                    dot_dict[row_num][i] = line[i]
                    ver_dict[i][row_num] = line[i]
                    connected[line[i]] = 0
                    
                    if greater(line[i], largest):
                        largest = line[i]
                        large_coord = (row_num, i)
                    if line[i] == '0':
                        zero_coord = (row_num, i)
            row_num += 1
        else:
            solve(dot_dict, ver_dict, row_num, col_num, large_coord,zero_coord)
            print()
            dot_dict = defaultdict(dict) #reset all settings for next map
            row_num = 0
            col_num = 0
            largest = '.'
    solve(dot_dict, ver_dict, row_num, col_num, large_coord,zero_coord)
            
