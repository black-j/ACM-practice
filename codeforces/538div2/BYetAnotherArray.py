
if __name__ == '__main__':
    n,m,k = [int(i) for i in input().strip().split()]
    nums = [int(i) for i in input().strip().split()]
    beauty_num = m*k
    num_sort = sorted(nums,reverse= True)[:beauty_num]
    
    num_dict = dict()
    for i in num_sort:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    counter = 0
    ans = []
    for i in range(n):
        if nums[i] in num_dict and num_dict[nums[i]] > 0:
            counter += 1
            num_dict[nums[i]] -= 1
        if counter >= m:
            ans.append(i + 1)
            counter = 0
    print(sum(num_sort))
    print(' '.join(str(i) for i in ans[:-1]))
