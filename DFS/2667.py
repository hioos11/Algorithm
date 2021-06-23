https://www.acmicpc.net/problem/2667
  


n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


apart = 2
result = [0]

def dfs(i, j, graph, apart, result):


    if i >= n or j >= n or i < 0 or j < 0:
        return False

    if graph[i][j] == 1:
        graph[i][j] = apart
        result[apart-2] += 1

        # print(result)

        # for a in graph:
        #     print(a)
        #
        # print()

        dfs(i + 1, j, graph, apart, result)
        dfs(i - 1, j, graph, apart, result)
        dfs(i, j + 1, graph, apart, result)
        dfs(i, j - 1, graph, apart, result)
        return True




for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # print(i, j)
            if dfs(i, j, graph, apart, result) == True:
                apart += 1
                result.append(0)

result.remove(0)

print(len(result))
result.sort()
for i in result:
    print(i)
