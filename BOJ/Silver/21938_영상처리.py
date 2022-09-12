from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()

    q.append([i, j])
    arr[i][j] = 1

    while q:
        i, j = q.popleft()

        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 255:
                q.append([ni, nj])
                arr[ni][nj] = 1

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

# 세 가지 픽셀값을 평균내어 T보다 크거나 같으면 255, 작으면 0으로 입력하는 arr 만들기
arr = [[]*M for _ in range(N)]
for i in range(N):
    for j in range(0, M*3, 3):
        tmp = sum(mat[i][j:j+3]) / 3
        if tmp >= T:
            arr[i].append(255)
        else:
            arr[i].append(0)

ans = 0
for i in range(N):
    for j in range(M):
        # 값이 255라면 물체로 인식
        if arr[i][j] == 255:
            bfs(i, j)
            ans += 1
print(ans)

'''
3 3
255 255 255 255 255 255 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255
101
'''