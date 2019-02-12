def find_components(i,j,visited,row,col,matrix):
    if i >= row or i < 0 or j >= col or j < 0 or matrix[i][j] == 'W':
        return
    elif (i,j) not in visited:
        visited.add((i,j))
        find_components(i,j+1,visited,row,col,matrix)
        find_components(i,j-1,visited,row,col,matrix)
        find_components(i+1,j,visited,row,col,matrix)
        find_components(i-1,j,visited,row,col,matrix)
if __name__ == '__main__':
    row,col = [int(i) for i in input().strip().split()]
    matrix = []
    for i in range(row):
        string = input().strip()
        matrix.append([])
        for cell in string:
            matrix[i].append(cell)
        
    visited = set()
    count = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 'L':
                if (i,j) not in visited:
                    count += 1
                    find_components(i,j,visited,row,col,matrix)
    print(count)
