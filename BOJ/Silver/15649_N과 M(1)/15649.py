# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * (N + 1)

arr = []
def dfs(n, num):
    if n == M:
        arr.append(num)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, num + [i])
            visited[i] = 0

dfs(0, [])
[print(*x) for x in arr]