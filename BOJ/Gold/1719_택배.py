# 정점 간의 간선은 두 집하장 간에 화물 이동이 가능함을 나타냄 / 가중치는 이동에 걸리는 시간
# 경로 표의 의미
    # 4행 5열의 6 : 4번 집하장에서 5번 집하장으로 최단 경로를 가기 위해서는 제일 먼저 6번 집하장으로 이동해야 한다는 의미

import sys
input = sys.stdin.readline
INF = int(1e9)
n, m  = map(int, input().split())   # n: 집하장 개수(200이하) / m: 집하장 간 경로 개수(10000이하)
graph = [[INF] *(n+1) for _ in range(n+1)]  # 노드별 갈 수 있는 최단 거리 저장
result = [['-']*(n+1) for _ in range(n+1)]  # 최소 경로에서 가장 먼저 방문해야 하는 노드 저장

# 각 간선에 대한 가중치 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = graph[b][a] = w
    result[a][b] = str(b)
    result[b][a] = str(a)

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 자기 자신으로 간다면 제외
            if i == j: continue
            # k를 거쳐서 갔을 때 최단 거리가 도출되는 경우
            if graph[i][j] > graph[i][k] + graph[k][j]:
                # 최단 거리 갱신
                graph[i][j] = graph[i][k] + graph[k][j]
                # k로 가기 위해 가장 먼저 방문해야 하는 노드 업데이트
                result[i][j] = result[i][k]

for i in range(1, n+1):
    print(*result[i][1:])