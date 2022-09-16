di = [-1,1,0,0,-1,-1,1,1]
dj = [0,0,-1,1,-1,1,-1,1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 한 변 길이(4, 6, 8) / M : 플레이어가 돌을 놓는 횟수
    arr = [[0]*N for _ in range(N)]
    # 1이면 흑돌 / 2면 백돌
    arr[N//2][N//2] = 2
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2] = 1
    arr[N//2-1][N//2-1] = 2

    for _ in range(M):
        si, sj, target = map(int, input().split())
        si -= 1 ; sj -= 1
        arr[si][sj] = target
        k = 0
        i = si ; j = sj
        tmp = []
        while k < 8:
            ni = i + di[k] ; nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in [1,2]:
                if arr[ni][nj] == target:
                    for ci, cj in tmp:
                        arr[ci][cj] = target
                    tmp = []
                    k += 1
                    i = si ; j =sj
                    continue
                else:
                    tmp.append([ni, nj])
                    i = ni ; j = nj
            else:
                tmp = []
                k += 1
                i = si ; j = sj
    b = w = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1
    print(f'#{tc} {b} {w}')

'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''