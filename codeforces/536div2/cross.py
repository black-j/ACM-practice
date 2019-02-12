def find(x,y,matrix):
    if x + 1 >= len(matrix) or x-1<0 or y+1 >= len(matrix) or y - 1<0:
        return False
    return matrix[x-1][y-1] == 'X' and matrix[x-1][y+1] == 'X' and matrix[x+1][y-1] == 'X' and matrix[x+1][y+1] == 'X'
if __name__ == '__main__':
    num = int(input().strip())
    matrix = []
    for i in range(num):
        matrix.append([])
        line = input().strip()
        for j in range(num):
            matrix[i].append(line[j])
    ans = 0
    for i in range(num):
        for j in range(num):
           if matrix[i][j] == 'X':
               if find(i,j,matrix):
                   ans += 1
    print(ans)
    
