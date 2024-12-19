import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

result = []
def dfs(n, numLst):
    global result
    if n == M:
        result.append(numLst)
        return
    
    for i in range(1, N + 1):
        dfs(n + 1, numLst + [i])

dfs(0, [])
[print(*x) for x in result]