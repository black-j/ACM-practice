
if __name__ == '__main__':
    num_list = [i+1 for i in range(int(input().strip()))]
    gas_list = [int(i) for i in input().strip().split()]
    gas_list.sort()
    mini = 1
    explod = False
    for i in range(len(num_list)):
        if gas_list[i] > num_list[i]:
            explod  = True
            break
        else:
            
            result = gas_list[i]/num_list[i]
            if result < mini:
                mini = result
    if explod:
        print('impossible')
    else:
        print(mini if mini != 0 else 0)
