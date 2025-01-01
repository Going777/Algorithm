from collections import deque
import sys
input = sys.stdin.readline

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향
# 1: 익은 토마토
# 0: 익지 않은 토마토
# -1: 토마토가 없는 칸

def bfs():
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()

    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1: # 익은 토마토 큐에 추가
                    visited[h][i][j] = 1
                    q.append([h, i, j])
                elif arr[h][i][j] == 0: # 안 익은 토마토 개수 세기
                    cnt += 1
    
    while q:
        ch, ci, cj = q.popleft()

        # 6방향, 범위내, 안 익은 토마토(arr[] == 0), 미방문 
        for dh, di, dj in [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)]:
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < H and  0<= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and not visited[nh][ni][nj]:
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1
                q.append([nh, ni, nj])
                cnt -= 1 # 안익은 토마토 1개 익음

    if cnt == 0:
        return visited[ch][ci][cj] - 1
    else:
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)
