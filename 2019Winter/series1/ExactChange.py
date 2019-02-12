'''dp problem
    coin change variation
    use python2 to avoid TLE error'''
if __name__ == '__main__':
    test_case = []
    num = int(input().strip())
    for _ in range(num):
        price = int(input().strip())
        num = int(input().strip())
        cents = [[0 for i in range(price + 1)]]
        counts = [[0 for i in range(price + 1)]]
        coins = [0]
        for _ in range(num):
            coins.append(int(input().strip()))
            cents.append([0 for i in range(price + 1)])
            counts.append([0 for i in range(price+1)])
        coins.sort()
        for i in range(1,len(coins)):
            for j in range(1,price + 1):
                if cents[i-1][j] == 0:
                    if coins[i] >= j:
                        cents[i][j] = coins[i]
                        counts[i][j] = 1
                    elif coins[i] + cents[i-1][j-coins[i]] >= j:
                        cents[i][j] = coins[i] + cents[i-1][j-coins[i]]
                        counts[i][j] = 1 + counts[i-1][j-coins[i]]
                else:
                    if coins[i] > j:
                        if cents[i-1][j] - j >= coins[i] - j:
                            cents[i][j] = coins[i]
                            counts[i][j] = 1
                        else:
                            cents[i][j] = cents[i-1][j]
                            counts[i][j] = counts[i-1][j]
                    else:
                        new = abs(j-coins[i]-cents[i-1][j-coins[i]])
                        old = abs(j-cents[i-1][j])
                        if new < old:
                            cents[i][j] = coins[i] + cents[i-1][j-coins[i]]
                            counts[i][j] = counts[i-1][j-coins[i]] + 1
                        elif old < new:
                            cents[i][j] = cents[i-1][j]
                            counts[i][j] = counts[i-1][j]
                        else:
                            cents[i][j] = cents[i-1][j]
                            counts[i][j] = min(counts[i-1][j],1+counts[i-1][j-coins[i]])
##                if j > cents[i][j-1]:
##                    if j > coins[i] + cents[i-1][j]:
##                        cents[i][j] = cents[i-1][j] + coins[i]
##                    elif coins[i] <= j:
##                        if cents[i - 1][j] < j:
##                            cents[i][j] = coins[i]+cents[i][j - coins[i]]
##                        else:
##                            cents[i][j] = min(cents[i-1][j],coins[i]+cents[i][j - coins[i]])
##                    else:
##                        if cents[i-1][j] < j:
##                            cents[i][j] = coins[i]
##                        else:
##                            cents[i][j] = min(cents[i-1][j],coins[i])
##                else:
##                    cents[i][j] = cents[i][j-1]
##        coin_count = 0
##        back = len(coins) - 1
##        temp = cents[-1][-1]
##        j = price
##        #print(coins[back])
##        while temp > 0 and back > 0:
##            #print(temp,back)
##            if temp - coins[back] == 0:
##                coin_count += 1
##                break
##            if j - coins[back] >= 0 and temp - coins[back] == cents[back][j - coins[back]]:
##                temp -= coins[back]
##                j -= coins[back]
##                coin_count += 1
##                
##            back -= 1
        #print(cents, price)   
        print(cents[-1][-1],counts[-1][-1])
   
            
