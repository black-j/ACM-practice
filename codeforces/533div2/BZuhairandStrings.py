
if __name__ == '__main__':
    n,k = [int(i) for i in input().strip().split()]
    string = input().strip()
    ctr = 1
    str_dict = dict()
    if len(string) == 1:
        if k == 1:
            print(1)
    else:
        if k == 1:
            for i in range(len(string)):
                if string[i] not in str_dict:
                    str_dict[string[i]] = 1
                else:
                    str_dict[string[i]] += 1
        else:
            for i in range(1,len(string)):
                if string[i-1] == string[i]:
                    ctr += 1
                else:
                    ctr = 1
                if ctr == k:
                    if string[i] not in str_dict:
                        str_dict[string[i]] = 1
                    else:
                        str_dict[string[i]] += 1
                    ctr = 0
            
            
                
            
            

        print(0 if str_dict == dict() else max(str_dict.values()))
