def dijkstra(s):
    D = adjA[s][:]
    visited = [0]*N
    visited[s] = 1
    for _ in range(N-1):     # N-1개의 남은 노드 처리
        # 미방문 노드 중 최소거리 노드 번호 찾기 & 방문 표시
        mn = INF
        i_mn = 0
        for i in range(1, N):
            if visited[i] == 0 and D[i] < mn:
                i_mn = i
                mn = D[i]
        visited[i_mn] = 1

        # 모든 노드를 대상으로 최단거리 갱신
        for i in range(N):
            D[i] = min(D[i], D[i_mn]+adjA[i_mn][i])

    return D[N-1]

T = int(input())
INF = 100000
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjA = [[INF]*N for _ in range(N)]
    for i in range(N):
        adjA[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjA[s][e] = w
    ans = dijkstra(0)
    print(f'#{tc} {ans}')

'''
1
6 10
0 1 3
0 2 4
1 3 5
2 1 1
2 3 4
2 4 5
3 4 3
3 5 4
4 0 3
4 5 4
'''