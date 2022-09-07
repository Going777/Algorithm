from collections import deque

def bfs(idx_lst):
    q = deque(idx_lst)
    time = 0

    while q:
        # 정해진 시간초가 되면 정답 위치의 바이러스 상태 반환
        if time == S:
            return arr[X-1][Y-1]    # 가장 왼쪽위를 (1,1)로 지정하고 있으므로, 인덱스를 맞춰주기 위해 1씩 빼줌

        # 현재 q에 들어있는 모든 원소들에 대하여 작업해주어야 1초가 지나게 되는 것
        for _ in range(len(q)):
            k, i, j = q.popleft()

            for (di, dj) in [(-1,0), (1,0), (0,-1), (0,1)]:     # 상하좌우 탐색
                ni = i + di; nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    q.append([k, ni, nj])
                    arr[ni][nj] = k     # 방문표시 및 바이러스 번호 표시
        time += 1

N, K = map(int, input().split())    # N: NxN 정방행렬 / K: 바이러스 max 번호(1~K번까지 하나씩 존재)
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split()) # S: 시간 / X,Y: 위치

starts_idx = []  # 탐색열
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:  # 원소값이 0이 아니라면 바이러스가 있는 것 -> 바이러스 번호와 위치를 탐색열에 추가
            starts_idx.append([arr[i][j], i, j])

starts_idx = sorted(starts_idx) # 번호가 낮은 바이러스부터 먼저 증식하므로 바이러스 번호 기준 (0번째 인덱스) 오름차순 정렬 필요
ans = bfs(starts_idx)
print(ans)