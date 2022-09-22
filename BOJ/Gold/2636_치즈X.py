N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 치즈가 놓여있으면 1, 안놓여있으면 0
# 제일 바깥에는 치즈 놓이지 않음
c = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + di ; nj = j + dj
                if arr[ni][nj] == 0:
                    c.append([i, j])
                    break
