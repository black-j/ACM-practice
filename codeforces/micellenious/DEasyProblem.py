'''A good dp practive of figuring out state and its transition
    ans[i][j] represent at from 0 to ith position of input string
    the minimum charater to change so that there are no sequence
    of string 'hard' from 0 to jth position that appears in input string
'''
if __name__ == '__main__':
    num = int(input().strip())
    string = input().strip()
    cost = [int(i) for i in input().strip().split()]
    hard_list = ['.','h','a','r','d']
    ans = [[10000000000000000000000000000,0,0,0,0] for i in range(num+1)] #Big enough to accomodate all answers
    for i in range(1,num+1):
        for j in range(1,5):
            if string[i-1] == hard_list[j]:
                ans[i][j] = min(ans[i-1][j-1],ans[i-1][j] + cost[i-1])
            else:
                ans[i][j] = ans[i-1][j]

    print(ans[-1][-1])
