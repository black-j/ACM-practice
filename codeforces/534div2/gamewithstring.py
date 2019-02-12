'''linked list'''
if __name__ == '__main__':
    counter = 0
    string = input().strip()
    index = 0
    index2 = 1
    while index < len(string):
        if string[index1] == string[index2]:
            counter += 1
            index += 2
        else:
            index += 1

    print('No' if counter%2 == 0 else 'Yes')
