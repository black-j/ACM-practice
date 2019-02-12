vowels = set(['a','e','i','o','u'])
if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    if len(s) != len(t):
        print('No')
    else:
        yes = True
        for i in range(len(s)):
            if s[i] in vowels and t[i] not in vowels:
                yes = False
                break
            elif s[i] not in vowels and t[i] in vowels:
                yes = False
                break
        print('Yes' if yes else 'No')
