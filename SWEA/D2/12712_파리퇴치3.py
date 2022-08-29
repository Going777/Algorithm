# import sys
# sys.stdin = open('input.txt', 'r')

# 파리 퇴치3
# di = [-1, 1, 0, 0] # 상/하/좌/우
# dj = [0, 0, -1, 1]
# di_2 = [-1, 1, -1, 1] # 우상/우하/좌상/좌하
# dj_2 = [1, 1, -1, -1]
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_cnt = 0
#
#     for i in range(N):
#         for j in range(N):
#             tmp = arr[i][j] # 상하좌우 합 / 초기값은 현재 자리값
#             tmp_2 = arr[i][j] # 대각선 합 / 초기값은 현재 자리값
#             for d in range(4):
#                 # 방향 바꿀때마다 위치 초기화
#                 ti, tj = i, j
#                 ti_2, tj_2 = i, j
#                 for _ in range(M-1): # M번까지 뻗어나갈 수 있음
#                     ni = ti + di[d]; nj = tj + dj[d] # 상하좌우 탐색
#                     ni_2 = ti_2 + di_2[d]; nj_2 = tj_2 + dj_2[d] # 대각선 탐색
#                     if (0 <= ni < N) and (0 <= nj < N):
#                         tmp += arr[ni][nj]
#                         ti = ni; tj = nj # 위치 갱신
#                     if (0 <= ni_2 < N) and (0 <= nj_2 < N):
#                         tmp_2 += arr[ni_2][nj_2]
#                         ti_2 = ni_2; tj_2 = nj_2 # 위치 갱신
#             if max_cnt < tmp:
#                 max_cnt = tmp
#             if max_cnt < tmp_2:
#                 max_cnt = tmp_2
#
#     print(f"#{t} {max_cnt}")



# 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

# 우상/우하/좌상/좌하
di2 = [-1,1,-1,1]
dj2 = [1,1,-1,-1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = tmp2 = arr[i][j]
            for m in range(1, M):
                for k in range(4):
                    ni = i + di[k]*m; nj = j + dj[k]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        tmp += arr[ni][nj]

                    ni2 = i +di2[k]*m; nj2 = j + dj2[k]*m
                    if 0 <= ni2 < N and 0 <= nj2 < N:
                        tmp2 += arr[ni2][nj2]

            ans = max(ans, tmp, tmp2)

    print(f"#{tc} {ans}")

'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''

