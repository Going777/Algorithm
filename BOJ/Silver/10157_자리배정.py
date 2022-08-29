def solve():
    n = 1
    k = 0
    i = M-1; j = 0

    if K > N*M:
        return [0]

    while True:
        arr[i][j] = n
        if n == K:
            return [j+1, M-i]
        if n == M*N:
            return [0]
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
            n += 1
            i = ni; j = nj
        else:
            k = (k+1) % 4

N, M = map(int, input().split())    # N: 가로, M: 세로
K = int(input())    # 대기번호
arr = [[0]*N for _ in range(M)]

# 방향(상우하좌)
di = [-1,0,1,0]
dj = [0,1,0,-1]

ans = solve()

print(*ans)

'''
7 6
11

7 6
87

100 100
3000
'''