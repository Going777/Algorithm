import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [False] * N

def dfs(n, numLst):
    if n == M:
        print(*numLst)
        return
    
    prev = -1
    for i in range(N):
        targetValue = numLst[-1] if numLst else 0 
        if not visited[i] and lst[i] != prev and targetValue <= lst[i]:
            visited[i] = True
            dfs(n + 1, numLst + [lst[i]])
            visited[i] = False
            prev = lst[i]

dfs(0, [])