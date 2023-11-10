class Graph:

    def __init__(self, node_list):

        self.length = len(node_list)
        self.matrix = [[0] * self.length for i in range(self.length)]

        for i in range(self.length -1):

            for j in range(i+1, self.length):

                if self.has_loop(node_list[i], node_list[j]):

                    self.matrix[i][j] = 1
                    self.matrix[j][i] = 1


    def has_loop(self,a,b):

    # n is the total number of two competitor
    #if the number is odd, it can go infinitly because it can't be
    #if an even number is not the power of 2, it can also have loop 
        if a==b:

            return False

        n = a + b

        if n % 2 == 1:

            return True

        else:

            if n > 0 and n & (n-1) == 0:

                return False

            else:

                return True


    def dfs(self,u,visited,match):

        if u is not None:

            for v in range(self.length):

                if self.matrix[u][v] == 1 and not visited[v]:

                    visited[v] = True

                    if match[v] is None or self.dfs(match[v],visited,match):

                        match[v] = u

                        return True
        return False

    def max_matching(self):

        match = [None] * self.length

        result = 0

        for i in range(self.length):

            visited = [False] * self.length

            if self.dfs(i,visited,match):

                result+=1

        return self.length - 2*(result/2)


def solution(banana_list):

    g = Graph(banana_list)

    return g.max_matching()

print(solution([1,1]))
print(solution([1, 7, 3, 21, 13, 19]))
print(solution([1,3,1]))
