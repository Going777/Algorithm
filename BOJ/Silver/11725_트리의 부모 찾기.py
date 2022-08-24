def bfs(s):
    q = []

    q.append(s)
    visited[s] = s

    while q:
        i = q.pop(0)

        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = i          # 자식 노드 방문 체크 배열에 부모 노드 정점을 할당

N = int(input())                        # 정점 개수
adjLst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

visited = [0]*(N+1)

bfs(1)

for idx in range(2,N+1):                # 2번째 정점부터 순서대로 부모 노드 출력
    print(visited[idx])