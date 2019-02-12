"""Again, getting TLE on Python3 and passed with Python2... Orz"""

if __name__ == '__main__':
    num = int(input().strip())
    digit_tree = {'count':0}
    for i in range(num):
        string = input().strip()
        temp = digit_tree
        for j in range(len(string)):
            if string[j] not in temp:
                temp[string[j]] = dict()
                temp[string[j]]['count'] = 1
                temp = temp[string[j]]
                if j == len(string) - 1:
                    print(0)
            else:
                
                if j == len(string) - 1:
                    print(temp[string[j]]['count'])
                temp[string[j]]['count'] += 1
                temp = temp[string[j]]


    
