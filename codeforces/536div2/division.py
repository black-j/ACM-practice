
if __name__ == '__main__':
    num = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    i,j = 0,num-1
    ans = 0
    nums.sort()
    while i < j:
        ans += (nums[i] + nums[j])**2
        i+=1
        j-=1
    print(ans)
