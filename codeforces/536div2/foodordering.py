
if __name__ == '__main__':
    food_num,cus_num = [int(i) for i in input().strip().split()]
    food_dict = dict()
    food_order = []
    line1 = [int(i) for i in input().strip().split()]
    line2 = [int(i) for i in input().strip().split()]
    for i in range(1,food_num+1):
        food_dict[i] = [line1[i-1],line2[i-1]]
    food_order = sorted(food_dict,key = lambda x:(food_dict[x][1],x))
    #print(food_order)
    ans = 0
    cheap_index = 0
    done = False
    for i in range(cus_num):
        ans = 0
        kind,kind_num = [int(i) for i in input().strip().split()]
        if cheap_index == food_num - 1 and food_dict[food_order[cheap_index]][0] <= 0:
            print(0)
        else:
            remain = food_dict[kind][0] - kind_num
            if remain >= 0:
                food_dict[kind][0] = remain
                print(kind_num*food_dict[kind][1])
            else:
                
                temp = (food_dict[kind][0])*food_dict[kind][1]
                food_dict[kind][0] = 0
                remain = abs(remain)
                while remain >= 0:
                    if cheap_index > food_num - 1:
                        done = True
                        break
                    holder = remain
                    remain = food_dict[food_order[cheap_index]][0] - remain
                    if remain >= 0:
                        food_dict[food_order[cheap_index]][0] = remain
                        temp += holder*food_dict[food_order[cheap_index]][1]
                        break
                    else:
                        remain = abs(remain)
                        temp += food_dict[food_order[cheap_index]][0]*food_dict[food_order[cheap_index]][1]
                        food_dict[food_order[cheap_index]][0] = 0
                        cheap_index += 1
                if not done:
                    ans+=temp
                    print(temp)
                else:
                    print(0)
        
