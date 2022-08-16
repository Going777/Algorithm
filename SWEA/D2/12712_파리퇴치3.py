import sys
sys.stdin = open('input.txt', 'r')

# 파리 퇴치3
di = [-1, 1, 0, 0] # 상/하/좌/우
dj = [0, 0, -1, 1]
di_2 = [-1, 1, -1, 1] # 우상/우하/좌상/좌하
dj_2 = [1, 1, -1, -1]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            tmp = arr[i][j] # 상하좌우 합 / 초기값은 현재 자리값
            tmp_2 = arr[i][j] # 대각선 합 / 초기값은 현재 자리값
            for d in range(4):
                # 방향 바꿀때마다 위치 초기화
                ti, tj = i, j
                ti_2, tj_2 = i, j
                for _ in range(M-1): # M번까지 뻗어나갈 수 있음
                    ni = ti + di[d]; nj = tj + dj[d] # 상하좌우 탐색
                    ni_2 = ti_2 + di_2[d]; nj_2 = tj_2 + dj_2[d] # 대각선 탐색
                    if (0 <= ni < N) and (0 <= nj < N):
                        tmp += arr[ni][nj]
                        ti = ni; tj = nj # 위치 갱신
                    if (0 <= ni_2 < N) and (0 <= nj_2 < N):
                        tmp_2 += arr[ni_2][nj_2]
                        ti_2 = ni_2; tj_2 = nj_2 # 위치 갱신
            if max_cnt < tmp:
                max_cnt = tmp
            if max_cnt < tmp_2:
                max_cnt = tmp_2

    print(f"#{t} {max_cnt}")