import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def dfs(n, numLst):
    if n == M:
        print(*numLst)
        return
    
    prev = -1  # 이전 값을 저장하여 중복 체크
    for i in range(N):
        if not visited[i] and lst[i] != prev:
            visited[i] = True
            dfs(n + 1, numLst + [lst[i]])
            visited[i] = False
            prev = lst[i]  # 이전 값을 갱신

visited = [False] * N
dfs(0, [])
