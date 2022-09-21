import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    visited[n] = 1
    for i in adjLst[n]:
        if not visited[i]:
            dfs(i)
            visited[n] += visited[i]

N, R, Q = map(int, input().split())     # N: 정점 수 / R: 루트 번호 / Q: 쿼리 수
adjLst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

visited = [0]*(N+1)
dfs(R)

for _ in range(Q):
    print(visited[int(input())])