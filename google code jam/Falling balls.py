'''solved'''
import sys

def solve():
    open_file = open(input())
    test_num = int(open_file.readline().rstrip())
    
    for _ in range(test_num):
        length = int(open_file.readline().rstrip())
        result_list = [int(i) for i in open_file.readline().rstrip().split()]
        done_list = [1 for _ in range(length)]
        print('Case #' + str(_+1)+": ",end = '')
        if result_list[0] == 0 or result_list[-1] == 0:
            print("IMPOSSIBLE")
        else:
            answer = construct(result_list, done_list, length)
            answer.append(['.' for _ in range(length)])
            print(len(answer))
            for i in answer:
                for j in i:
                    print(j, end = '')
                print()
    
def construct(result_list:list, done_list:list, length:int):
    answer = []
    devide_index = 0
    for i in range(length):
        # print(devide_index)
        while(result_list[i] != 0):
            if devide_index == i:
                devide_index += 1
                result_list[i] -= 1
                
            elif devide_index > i:
                temp = devide_index + result_list[i]
                for high,j in enumerate(range(devide_index + result_list[i]-1,i,-1),0):
                    #print(j)
                    if len(answer) <= high:
                        answer.append(['.' for _ in range(length)])
                    #print(answer)
                    answer[high][j] = '/'
                result_list[i] = 0
                devide_index = temp
                
            elif devide_index < i:
                temp = devide_index
                for high,j in enumerate(range(temp, i),0):
                    #print(j, devide_index)
                    if result_list[i] == 0:
                        break
                    if len(answer) <= high:
                        answer.append(['.' for _ in range(length)])
                    devide_index += 1
                    answer[high][j] = '\\'
                    result_list[i] -= 1
    return answer
                    
            
if __name__ == '__main__':
    solve()
