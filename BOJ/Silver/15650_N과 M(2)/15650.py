import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N + 1)
result = []

def dfs(n, start, num):
    if n == M:
        result.append(num)
        return
    for i in range(start, N +1):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, i + 1, num + [i])
            visited[i] = 0

dfs(0, 1, [])
[print(*x) for x in result]