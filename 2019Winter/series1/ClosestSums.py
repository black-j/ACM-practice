import bisect

if __name__ == '__main__':
    index = 0
    while True:
        try:
            
            n = int(input().strip())
            nums = []
            for _ in range(n):
                nums.append(int(input().strip()))
                nums.sort()
            
            index += 1
            print('Case {}:'.format(index))
            m = int(input().strip())
            printed = False
            for i in range(m):
                q = int(input().strip())
                small = 10000000
                for k in range(len(nums)):
                    j = bisect.bisect(nums,k+1,len(nums),q-nums[k])
                    print(j)
                    if abs(q-nums[j]-nums[k]) < small:
                        small = abs(q-nums[j]-nums[k])
                        second = nums[j] + nums[k]
                    
                    try:
                        if abs(q-nums[j+1]-nums[k]) < small:
                            small = abs(q-nums[j+1]-nums[k])
                            second = nums[j+1] + nums[k]
                    except:
                        pass
                    try:
                        if abs(q-nums[j-1]-nums[k]) < small:
                            small = abs(q-nums[j-1]-nums[k])
                            second = nums[j-1] + nums[k]
                    except:
                        pass
                print('Closest sum to {} is {}.'.format(q,second))        
        except EOFError:
            break
