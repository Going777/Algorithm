'''
낮은 번호의 정점을 우선적으로 방문한다!!
'''
def bfs(n):
    q = []
    visited = [0]*(V+1)
    q.append(n)
    visited[n] = 1
    while q:
        i = q.pop(0)
        result.append(i)
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjLst = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)
    # 낮은 번호를 먼저 방문해야하므로, 정렬 필요!
    for lst in adjLst:
        lst.sort()
    result = []
    bfs(1)
    print(f'#{tc}', *result)

'''
1
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''