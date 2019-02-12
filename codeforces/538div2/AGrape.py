
if __name__ == '__main__':
    needs = [int(i) for i in input().strip().split()]
    grapes = [int(i) for i in input().strip().split()]
    yes = True
    remain = grapes[0] - needs[0]
    if remain < 0:
        print('No')
    else:
        grapes[0] = remain
        remain = grapes[0] - needs[1]
        if remain < 0:
            grapes[0] = 0
            remain = abs(remain)
            remain = grapes[1] - remain
            if remain < 0:
                print('No')
            else:
                grapes[1] = remain
                if needs[2] - grapes[0] - grapes[1] - grapes[2] <=0:
                    print('YES')
                else:
                    print('NO')
        else:
            grapes[0] = remain
            if needs[2] - grapes[0] - grapes[1] - grapes[2] <=0:
                print('YES')
            else:
                print('NO')
