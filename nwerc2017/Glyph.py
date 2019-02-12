
def solve(coord_list, right_vertex):
   square_eval(coord_list, right_vertex)

def square_eval(coord_list, right_vertex):
    positive = [[abs(j) for j in coord_list[i]] for i in range((len(coord_list)))]
    print([i[0] + i[1] for i in positive])
    s = 0
    l = 0
    
    for i in range(len(positive)):
        if positive[i][0]*positive[i][1] > 0 and positive[i][0]*positive[i][1] < positive[s][0]*positive[s][1]:
            s = i
        if positive[i][0]*positive[i][1] > positive[s][0]*positive[s][1]:
            l = i
    
    print(positive[s], positive[l])

if __name__ == "__main__":

    num = int(input())
    right_vertex = []
    coord_list = []
    
    for i in range(num):
        line = [int(i) for i in input().strip().split()]
        if line[1] == 0:
            right_vertex.append(line)
        coord_list.append(line)

    print(coord_list, right_vertex)
    solve(coord_list, right_vertex)
