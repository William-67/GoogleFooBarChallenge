from collections import deque
import copy

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(row, col, m):

    NumRows = len(m)
    NumCols = len(m[0])

    visited = [[0 for _ in range(NumCols)] for _ in range(NumRows)]

    visited[row][col] = 1

    queue = deque()

    #must start from 0  
    queue.append((row, col))

    while queue:

        r, c = queue.popleft()

        for dr, dc in directions:

            next_r, next_c = (r + dr, c + dc)

            if 0 <= next_r < NumRows and 0 <= next_c < NumCols and visited[next_r][next_c] == 0:

                if m[next_r][next_c] == 0:

                    queue.append((next_r, next_c))

                visited[next_r][next_c] = visited[r][c] + 1 #visited

    return visited

def compare_and_get_smaller(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return min(num1, num2)

def solution(m):

    row = len(m)
    col = len(m[0])
    entr = bfs(0,0,m)
    exit = bfs(row-1,col-1,m)
    best = compare_and_get_smaller(entr[row-1][col-1],exit[0][0])

    for i in range(row):

        for j in range(col):

            tmp_m = copy.deepcopy(m)

            if tmp_m[i][j] == 1:
                
                tmp_m[i][j] = 0

                t_entr = bfs(0,0,tmp_m)
                t_exit = bfs(row-1,col-1,tmp_m)

                tmp_best = compare_and_get_smaller(t_entr[row-1][col-1],t_exit[0][0])
                best = compare_and_get_smaller(tmp_best,best)

    return best

print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))

m = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(bfs(0,0,m))
print(bfs(5,5,m))

k = [[0 for _ in range (5)] for _ in range(5) ]
k[2][3] = 1

print(bfs(0,0,k))

l = [[0,1],[1,0]]

print(bfs(0,0,l))
print(solution(l))