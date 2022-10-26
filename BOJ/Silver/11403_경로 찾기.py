'''
가중치 없는 방향 그래프 G가 주어졌을 때,
모든 정점에 대해서 i에서 j로 가는 경로가 있는지 없는지 구하라
'''
from collections import deque

def bfs(s):
    q = deque()
    check = [0 for _ in range(N)]   # 방문 여부 체크
    q.append(s)

    while q:
        i = q.popleft()                             # 탐색행
        for j in range(N):                          # 탐색행의 모든 열 검사
            if check[j] == 0 and adjA[i][j] == 1:   # 방문하지 않았으며, 연결된 정점이라면
                q.append(j)                         # 탐색행에 추가
                check[j] = 1                        # 방문 표시
                visited[s][j] = 1                   # 가능 경로로 표시

N = int(input())    # 정점 개수
adjA = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]     # 경로 여부를 나타내는 배열

for s in range(N):  # 행 별로 처리
    bfs(s)

for v in visited:
    print(*v)

'''
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
'''