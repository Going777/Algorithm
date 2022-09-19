import sys
input = sys.stdin.readline

def dfs(n, depth):
    global isExist
    visited[n] = 1
    if depth == 4:
        isExist = True
        return
    for i in adjLst[n]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = 0

N, M = map(int, input().split())
adjLst = [[] for _ in range(N)]
visited = [0]*N
isExist = False
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

for i in range(N):
    dfs(i, 0)
    visited[i] = 0
    if isExist:
        break

if isExist:
    print(1)
else:
    print(0)