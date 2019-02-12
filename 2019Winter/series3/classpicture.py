import sys
sys.setrecursionlimit = 100000
def dfs(ans,name_list,name_dict,index):
    #print(ans, type(ans))
    if len(ans) == len(name_list):
        return ans
    for i in range(len(name_list)):
        if name_list[i] in ans:
            continue
        if name_list[index] not in name_dict[name_list[i]]:
            ans.append(name_list[i])
            ans = dfs(ans,name_list,name_dict,i)
    return ans
    
if __name__ == '__main__':
    while True:
        try:
            num = input().strip()
            if len(num) == 0:
                break
            num = int(num)
            name_list = []
            name_dict = dict()
            
            for i in range(num):
                name = input().strip()
                name_list.append(name)
                name_dict[name] = set()
            name_list.sort()
            if num == 1:
                print(name_list[0])
            else:
            
                num = int(input().strip())
                for i in range(num):
                    name1,name2 = input().strip().split()
                    name_dict[name1].add(name2)
                    name_dict[name2].add(name1)

                ans = []
                index = 1
                for k in range(len(name_list)):
                    ans = []
                    ans.append(name_list[k])
                    ans = dfs(ans,name_list,name_dict,k)
                    if len(ans) == len(name_list):
                        break
                if len(ans) == len(name_list):
                    print(' '.join(ans))
                else:
                    print('You all need therapy.')
        except:
            break
