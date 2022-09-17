from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, c):
    q = deque()

    q.append([i, j])

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == c:
                q.append([ni, nj])
                if c in ['B', 'RG']:
                    arr[ni][nj] = 1
                elif c == 'R':
                    arr[ni][nj] = 'RG'
                elif c == 'G':
                    arr[ni][nj] = 'RG'

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

b_cnt = r_cnt = g_cnt = 0
for i in range(N):
    for j in range(N):
        # 파란색 처리
        if arr[i][j] == 'B':
            b_cnt += 1
            bfs(i, j, 'B')
            arr[i][j] = 1       # 파란색은 한 번만 처리해주면 되므로, 1로 값 변경(방문처리)
        # 빨간색 처리
        elif arr[i][j] == 'R':
            r_cnt += 1
            bfs(i, j, 'R')
            arr[i][j] = 'RG'    # 적록을 함께 처리해주어야 하기 때문에 'RG'로 값 변경
        # 초록색 처리
        elif arr[i][j] == 'G':
            g_cnt += 1
            bfs(i, j, 'G')
            arr[i][j] = 'RG'    # 적록을 함께 처리해주어야 하기 때문에 'RG'로 값 변경

rg_cnt = 0
for i in range(N):
    for j in range(N):
        # 적록인 경우 처리
        if arr[i][j] == 'RG':
            rg_cnt += 1
            bfs(i, j, 'RG')
            arr[i][j] = 1

rgb = r_cnt+g_cnt+b_cnt
rg_b = rg_cnt+b_cnt
print(rgb, rg_b)

'''
5
RGRRB
GRRRB
GGGGB
RRRRR
GRGGG
'''