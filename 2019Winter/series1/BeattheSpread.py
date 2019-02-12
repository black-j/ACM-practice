from math import ceil

if __name__ == '__main__':
    num = int(input().strip())
    for _ in range(num):
        x,y = 0,0
        s,d = [int(i) for i in input().rstrip().split()]
        x = (s+d)/2
        y = s - x
        #print(x,y)
        if x < 0 or y < 0 or x != int(x) or y != int(y):
            print('impossible')
        else:
            print(int(x),ceil(y))
