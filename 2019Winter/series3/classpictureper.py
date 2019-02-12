import sys
from itertools import permutations as per
sys.setrecursionlimit = 100000
'''Again!!! use python2!!!'''
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

                index = 1
                length = len(name_list)
                ans = []
                #print(name_dict)
                for k in per(name_list):
                    has = True
                    #print(k)
                    for i in range(1,length):
                        if k[i-1] in name_dict[k[i]]:
                            has = False
                            break
                    if has:
                        ans = k
                        break
                    
                if has:
                    print(' '.join(ans))
                else:
                    print('You all need therapy.')
        except:
            break
