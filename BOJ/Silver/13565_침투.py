from collections import deque
di = [-1,1,0,0]; dj = [0,0,-1,1]
def bfs(sj):
    q = deque()

    q.append([0,sj])
    arr[0][sj] = 1

    while q:
        i, j = q.popleft()

        if i == M-1:
            return True

        for k in range(4):
            ni = i + di[k]; nj = j + dj[k]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                q.append([ni, nj])
                arr[ni][nj] = 1
    return False
M, N = map(int, input().split())    # M: 행 수 , N: 열 수
arr = [list(map(int, input())) for _ in range(M)]
ans = "NO"

for j in range(N):
    if arr[0][j] == 0:
        if bfs(j):
            ans = "YES"
            break

print(ans)

'''
5 6
010101
010000
011101
100011
001011
'''