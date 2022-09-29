'''
A도시에는 E개의 일방통행 도로구간이 있으며, 각 구간이 만나는 연결지점에는 0~N의 번호가 붙어있다
0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리는?
(모든 연결지점을 거쳐야하는 것은 아니다)
'''
def dijkstra(s):
    D = [INF]*(N+1)
    visited = [0]*(N+1)
    visited[s] = 1
    for e,v in adjLst[s]:
        D[e] = v
    for _ in range(N):
        mn = INF
        mn_i = 0
        for i in range(1, N+1):
            if not visited[i] and D[i] < mn:
                mn_i = i
                mn = D[i]
        visited[mn_i] = 1
        for e,v in adjLst[mn_i]:
            D[e] = min(D[e], D[mn_i]+v)
    return D[-1]

INF = 10*1000
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())    # N: 마지막 연결지점 / E: 도로 개수
    adjLst = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int, input().split())
        adjLst[s].append([e,w])
    ans = dijkstra(0)
    print(f'#{tc} {ans}')

'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''