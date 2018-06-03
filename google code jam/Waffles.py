'''small dataset'''
def solve(rows:int. columns:int, waffle_list: list):
    total_number = 0
    for i in waffle_list:
        for j in i:
            if j == '@':
                total_number += 1

    
if __name__ == '__main__':
    open_file = open(input())
    test_num = int(open_file.readline().rstrip())
    
    for _ in range(test_num):
        rows, columns = [int(i) for i in open_file.readline().rstrip()][:2]
        waffle_list = []
        for _ in range(rows):
            result_list.append([i for i in open_file.readline().rstrip()])
        print(solve(rows,columns,waffle_list))
