import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited= [0] * N

def dfs(n, numLst):
    if n == M:
        print(*numLst)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, numLst + [lst[i]])
            visited[i] = 0

dfs(0, [])