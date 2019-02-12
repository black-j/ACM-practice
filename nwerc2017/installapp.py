def solve(app_list, num_app, free_disk):
    
    dp = []
    for i in range(num_app + 1):
       dp.append([])
       for j in range(free_disk + 1):
           dp[i].append(0)
           
    for i in range(1, num_app + 1):
        for j in range(1, free_disk + 1):
            if j - app_list[i - 1][1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - app_list[i - 1][1]] + \
                               app_list[i - 1][2],dp[i - 1][j])
                
    print(dp)
if __name__ == '__main__':
    num_ins, free_disk = [int(i) for i in input().strip().split()]
    app_list = []
    for i in range(num_ins):
        app_list.append([])
        line = [int(i) for i in input().strip().split()]
        app_list[i].append(i)
        app_list[i].append(max(line[0],line[1]))
        app_list[i].append(app_list[i][1] - line[1])
    app_list.sort(key = lambda x: x[1], reverse = True)
    solve(app_list, num_ins, free_disk) #include 0 in this case 
    print(app_list)
