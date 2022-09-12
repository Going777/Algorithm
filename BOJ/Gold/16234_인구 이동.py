import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global flag
    q = deque()

    q.append([i, j])
    visited[i][j] = 1   # 방문표시
    s_tmp = arr[i][j]   # 연합국 총 인구수
    loc = [[i, j]]      # 연합국에 포함될 위치

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:   # 상하좌우 탐색
            ni = i + di ; nj = j + dj
            # 범위내에 있고, 인구 차이가 N이상 R이하이고, 방문 안했다면
            if 0 <= ni < N and 0 <= nj < N and L <= abs(arr[i][j]-arr[ni][nj]) <= R and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1
                s_tmp += arr[ni][nj]
                loc.append([ni, nj])

    if len(loc) > 1:    # 연합국에 포함될 원소의 개수가 2개 이상이어야 인구이동 및 연합국 생성
        flag += 1               # flag값 1로 바꿔주기 (인구이동 일어남/연합국 생성)
        p = s_tmp // len(loc)   # 연합국 인구수 구하기
        for i, j in loc:        # 연합국 위치에 존재하는 국가의 인구수 업데이트
            arr[i][j] = p

N, L, R = map(int, input().split())     # N: 땅 크기(NxN) / L,R: 인구수 조건
# 국경선을 공유하는 두 나라의 인구수 차가 L명 이상, R명 이하라면 국경선을 연다
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    visited = [[0]*N for _ in range(N)] # 방문여부(그 다음번 인구이동을 체크할 때 초기화되어야 함)
    flag = 0                            # 인구이동이 일어나는지 여부(국경선을 열지 말지)를 저장하는 변수
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:       # 방문하지 않은 노드에 대해 진행
                bfs(i, j)
    if not flag:                       # 인구이동이 일어나지 않았다면 종료
        break
    cnt += 1                            # 인구이동이 일어났다면 cnt+1

print(cnt)