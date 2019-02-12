
if __name__ == '__main__':
    length,l,r = [int(i) for i in input().strip().split()]
    dp = []
    for i in range(l-1,r+1):
        dp.append([0 for i in range(length)])
    
    
    for line in dp:
        print(line)
            
