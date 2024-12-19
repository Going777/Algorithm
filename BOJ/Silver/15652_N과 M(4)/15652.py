import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
def dfs(n, numLst):
    if (n == M):
        result.append(numLst)
        return
    
    for i in range(1, N + 1):
        targetValue = numLst[-1] if numLst else 0            
        if targetValue <= i:
            dfs(n + 1, numLst + [i])

dfs(0, [])
[print(*x) for x in result]