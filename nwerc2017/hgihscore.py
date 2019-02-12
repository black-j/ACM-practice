'''
    solved!!!!!!!!!!
'''
from collections import defaultdict
letters = ['A','B','C','D','E','F','G','H','I','J','K', 'L', 'M', 'N',\
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']

letter_dict = {i:index for index,i in enumerate(letters)}

def solve(name):
    ''' not considering consecutive As in this naive version, the
        problem is also asking how many step does it take to convert name
        into A's using the same rule
    '''
    step_ctr = 0
    step_cost = find_turning(name)

   
    step_ctr += step_cost
    for letter in name:
        #print(step_ctr)
        if save_letter(letter):
            step_ctr += letter_dict['Z'] - letter_dict[letter] + 1
        else:
            step_ctr += letter_dict[letter]
    
    print(step_ctr)

def find_turning(name):
    a_count = 0
    value = 0
    first_a = 0
    step_cost = 0
    
    for i in range(0,len(name)):
        if name[i] == 'A' and i != 0:
            a_count += 1
            if a_count - first_a > value or a_count - (len(name) - (a_count + first_a + 1)) > value:
                value = max(a_count - first_a, a_count - (len(name) \
                                                            - (a_count + first_a + 1)))
        else:
            first_a = i
            a_count = 0

    sec_val = 0
    index = len(name) - 1
        
    step_cost = len(name) - 1 - value
##    if value > sec_val and value > head:
##        step_cost = len(name) - 1 - value
##    else:
##        step_cost = len(name) - 1 - (sec_val if sec_val>head else head)
            
    #print("STEP COST",step_cost)
    return step_cost
        
def save_letter(letter):
    if letter > 'M':
        return True
    return False

if __name__ == "__main__":

    num = int(input())
    
    for i in range(num):
        name = input().strip()
        solve(name)
