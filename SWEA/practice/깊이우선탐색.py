# 인접 리스트 방식
def dfs(n):
    for t in adjLst[n]:
        if not visited[t]:
            visited[t] = 1
            result.append(t)
            dfs(t)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjLst = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)
    result = []
    visited = [0]*(V+1)

    visited[1] = 1
    result.append(1)
    dfs(1)
    print(f'#{tc}', *result)

# --------------------------------------------------------------------

# 인접 행렬 방식
# def dfs(n):
#     if visited[n]:
#         return
#
#     visited[n] = 1
#     result.append(n)
#
#     for j in range(1, V+1):
#         if arr[n][j] == 1:
#             dfs(j)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = [[0]*(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         a, b = map(int, input().split())
#         arr[a][b] = 1
#         arr[b][a] = 1
#
#     visited = [0]*(V+1)
#     result = []
#     dfs(1)
#     print(f'#{tc}', *result)

'''
1
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''