from math import floor,ceil

if __name__ == "__main__":
    num = int(input().strip())
    if num == 1:
        print(1)
    else:
        print((ceil(num/2))*(floor(num/2)+1))
