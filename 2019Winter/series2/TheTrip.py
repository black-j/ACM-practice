import math
def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
if __name__ == '__main__':
    while True:
        num = int(input().strip())
        if num == 0:
            break
        m = list()
        total = 0
        for i in range(num):
            money = int(float(input().strip())*100)
            m.append(money)
            total += money
        if len(m) <= 1:
            print('$0.00')
        else:
            m.sort()
            cost = 0
            ave = total//num
            pen = total%num
            for i in range(num-1,-1,-1):
                
            
            print("${}".format(truncate(cost,2)))
        
        
