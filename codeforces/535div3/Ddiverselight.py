
if __name__ == '__main__':
    num = int(input().strip())
    string = input().strip()
    if num == 1:
        print(0)
        print(string)
    else:
        ans = [0 for i in range(num)]
        for n,i in enumerate(range(1,num),1):
            if string[i] == string[i-1]:
                if i >= 2 and string[i] == string[i-2]:
                    if ans[i-1] == ans[i-2]:
                        ans[i] = ans[i-1] + 1
                    else:
                        ans[i] = ans[i-1]
                else:
                    ans[i] = ans[i-1] + 1
            else:
                ans[n] = ans[n-1]
        #ans[-1] = ans[-2]
        ans_s = [string[0]]
        letter = ['R','B','G']
        for i in range(1,num-1):
            if ans[i] != ans[i-1]:
                for j in letter:
                    if j != string[i-1] and j!= string[i+1]:
                        ans_s.append(j)
                        break
            else:
                ans_s.append(string[i])
        if ans[-1] != ans[-2]:
            for j in letter:
                if j != string[-2]:
                    ans_s.append(j)
                    break
        else:
            ans_s.append(string[-1])
            
        print(ans[-1])
        print(''.join(ans_s))
