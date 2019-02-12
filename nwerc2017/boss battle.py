
def solve(num):
    num = num - 3
    ctr = 1
    while num > 0:
        ctr += 1
        num += 1
        num -= 2
    return ctr


if __name__ == "__main__":
    while True:
        num = int(input())
        print(solve(num))
