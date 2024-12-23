from collections import deque

def solution(n, computers):
    answer = 0
    adjLst = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if (i != j and computers[i][j]):
                adjLst[i].append(j)

    for i in range(n):
        if (not visited[i]):
            bfs(adjLst, i, visited)
            answer += 1

    return answer

def bfs(adjLst, v, visited):
    visited[v] = 1
    q = deque([v])

    while q:
        i = q.popleft()

        for t in adjLst[i]:
            if not visited[t]:
                visited[t] = 1
                q.append(t)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# def solution(n, computers):
#     def dfs(v):
#         visited[v] = True
#         for i in range(n):
#             if computers[v][i] and not visited[i]:
#                 dfs(i)

#     visited = [False] * n
#     answer = 0

#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             answer += 1

#     return answer

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))