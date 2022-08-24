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
def bfs(s):                     # s는 시작 정점
    q = []                      # 큐 생성
    visited = [0]*(V+1)         # 방문 표시 리스트 생성
    global result               # 출력 결과

    visited[s] = 1              # 시작 정점 방문 표시
    q.append(s)                 # 큐에 추가

    while q:                    # 큐가 빌때까지 반복
        t = q.pop(0)            # 큐에서 맨 앞 원소 t 꺼내기
        result.append(t)        # 해당 원소는 결과 리스트에 추가
        for i in adjLst[t]:     # 연결리스트에서 t와 연결된 모든 정점 탐색
            if not visited[i]:  # 방문하지 않은 정점이 있다면
                q.append(i)     # 큐에 추가
                visited[i] = 1  # 방문 표시

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V: 정점 개수, E: 간선 개수
    adjLst = [[] for _ in range(V+1)]
    result = []
    # 연결리스트 받기
    for _ in range(E):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)

    bfs(1)

    print(f"#{tc}", *result)