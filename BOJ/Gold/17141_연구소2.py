import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 상하좌우
di = [1,-1,0,0]
dj = [0,0,-1,1]

def bfs(step):
    visited = [[0]*N for _ in range(N)]
    q = deque()

    cnt = 0
    for si, sj in step:         # step으로 받은 M개의 바이러스 위치를 모두 q에 넣고 방문 표시 & 카운트+1
        q.append([si, sj])
        visited[si][sj] = 1
        cnt += 1

    while q:                    # q가 빌때까지 반복
        i, j = q.popleft()      # 탐색 시작할 인덱스 q로부터 받기

        for k in range(4):      # 상하좌우 방향 탐색
            ni = i + di[k]; nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == 0:    # 새 인덱스가 범위내에 있고, 방문한적이 없으며, 벽이 아니라면
                q.append([ni, nj])                  # 큐에 추가
                visited[ni][nj] = visited[i][j] + 1 # 방문표시 (단, 퍼지는 시간을 알기 위해 부모 노드의 방문표시값 +1)
                cnt += 1                            # 카운트 + 1

    if cnt == tot_target:           # 전체 개수에서 벽 개수 뺀만큼 카운트 되어야 모든 원소 다 방문하게 된 것
        return visited[i][j] - 1
    else:                           # 모두 돌았지만 tot_target만큼 카운트 되지 못했다면, 방문하지 못한 곳이 있는 것
        return N*N

N,M = map(int, input().split())    # N: 연구소 크기 / M: 바이러스 개수
# 0은 빈 칸, 1은 벽, 2는 바이러스 놓을 수 있는 칸
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []  # 바이러스 놓을 수 있는 후보군

wall_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:          # 바이러스 놓을 수 있는 위치
            arr[i][j] = 0           # 벽만 제외하고 모두 0으로 초기화
            virus.append([i, j])
        if arr[i][j] == 1:
            wall_cnt += 1           # 벽의 개수 카운트

ans = N*N
tot_target = N*N - wall_cnt
for step in combinations(virus, M): # 바이러스 놓을 수 있는 후보군에서 M개 개수만큼 뽑은 조합 만듦
    tmp = bfs(step)
    if ans > tmp:                   # 최소 ans값 찾기
        ans = tmp

if ans == N*N:                      # ans가 업데이트되지 않았다면, 모두 채울 수 없는 것
    ans = -1

print(ans)


'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''
