from math import floor
def solve(player_list, my_rate):
    while len(player_list) > 1:
        two_gen(player_list)

def two_gen(player_list):
    index = 0
    new_list = []
    for first,second in range(len(player_list)):
        new_list.append()

def  double win(int x,int y):
    return 1.0*a[x]/(a[x]+a[y]);


def my_gen(player_list):
    index = 0
    while index < len(player_list):
        if index >= player_list:
            yield player_list[index],0
        else:
            yield player_list[index], player_list[index+1]
        index += 2
        
if __name__ == "__main__":
    num = int(input())
    player_list = []
    my_rate = int(input().strip())
    for i in range(1,num):
        player_list.append(int(input().strip()))
    player_list.sort(reverse = True)
    player_list.append(my_rate)
    print(player_list, my_rate)
    solve(player_list, my_rate)


##    recursive_solve(player_list, my_rate, 0, 1)
##
##def recursive_solve(player_list, my_rate, first, last):
##    if first < last: 
##        mid = floor((len(player_list))/2)
##  
##        # Sort first and second halves 
##        recursive_solve(player_list[first:mid]) 
##        recursive_solve(player_list[mid+1:len(player_list)]) 
##        merge(arr, l, mid, r)
    
