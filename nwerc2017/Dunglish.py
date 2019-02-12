from collections import defaultdict
def solve(dun_dict, sentence):
    all_ctr = 1
    correct_ctr = 1
    correct = True
    no_one_correct = False
    
    for i in sentence:
        if 'correct' in dun_dict[i]:
            correct_ctr = correct_ctr * dun_dict[i]['correct']
        if 'incorrect' in dun_dict[i]:
            if correct:
                correct = False
                
            if  dun_dict[i].get('correct') == None and not no_one_correct:
                no_one_correct = True
                
            if 'correct' in dun_dict[i]:
                all_ctr = all_ctr * (dun_dict[i]['incorrect'] + \
                                     dun_dict[i]['correct'])
            else:
                all_ctr = all_ctr * dun_dict[i]['incorrect']
        else:
            all_ctr = all_ctr * dun_dict[i]['correct']

    if all_ctr > 1:
        if no_one_correct:
            print("{} correct".format(0))
            print("{} incorrect".format(all_ctr))
        else:
            print("{} correct".format(correct_ctr))
            print("{} incorrect".format(all_ctr - correct_ctr))
    else:
        print(' '.join([dun_dict[i]['word'] for i in sentence]))
        print("correct" if correct else "incorrect")

if __name__ == "__main__":

    num = int(input())
    sentence = input().strip().split()
    
    dun_dict = defaultdict(dict)
    for i in range(int(input().strip())):
        words = input().strip().split()
        dun_dict[words[0]]['word'] = words[1]
        if words[2] not in dun_dict[words[0]]:
            dun_dict[words[0]][words[2]] = 1
        else:
            dun_dict[words[0]][words[2]] += 1
        
    solve(dun_dict, sentence)
