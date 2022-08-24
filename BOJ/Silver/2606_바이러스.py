def bfs(s):
    global cnt
    visited = [0]*(N+1)
    q = []

    q.append(s)
    visited[s] = 1

    while q:
        i = q.pop(0)

        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1
                cnt += 1

N = int(input())        # 컴퓨터 수
E = int(input())        # 간선 수
adjLst = [[] for _ in range(N+1)]
cnt = 0
for _ in range(E):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

bfs(1)

print(cnt)