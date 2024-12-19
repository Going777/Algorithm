import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def dfs(n, numLst):
    if n == M:
        print(*numLst)
        return
    
    for i in range(N):
        targetValue = numLst[-1] if numLst else 0
        if (targetValue <= lst[i]):
            dfs(n + 1, numLst + [lst[i]])

dfs(0, [])