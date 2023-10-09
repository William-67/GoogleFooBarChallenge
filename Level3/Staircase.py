def solution(n):
    # Your code here
    staircase = [[0 for _ in range (n+1)] for _ in range(n+1)]

    staircase[0][0] = 1
    
    for i in range(1,n+1):
        for j in range(0, n+1):
            staircase[i][j] = staircase[i-1][j]
            if j >= i:
                staircase[i][j] += staircase[i-1][j-i]
    #remove the following line
    print(staircase)
    return staircase[i][j] -1
