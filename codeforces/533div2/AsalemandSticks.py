
if __name__ == '__main__':
    num = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    t = 0
    cost = 1000000
    for i in range(1,101):
        c = 0
        for j in nums:
            if j != i:
                c += abs(j - i) - 1
            else:
                pass
        if c < cost:
            cost = c
            t = i
    print(t,cost)
