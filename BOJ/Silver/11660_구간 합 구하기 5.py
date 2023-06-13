'''
NxN개의 수가 표에 채워져 있다
(x1,y1)부터 (x2,y2)까지 합을 구하라
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 표의 크기 / M: 합을 구해야 하는 횟수
arr = [[0]*(N+1)]
s_arr = [[0]*(N+1) for _ in range(N+1)]                       # 구간 합 리스트

# 원본 리스트 받기
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    arr.append(row)

# 구간 합 리스트 채우기
for i in range(1, N+1):
    for j in range(1, N+1):
        s_arr[i][j] = s_arr[i][j-1] + s_arr[i-1][j] - s_arr[i-1][j-1] + arr[i][j]

# 질의 값 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = s_arr[x2][y2] - s_arr[x1-1][y2] - s_arr[x2][y1-1] + s_arr[x1-1][y1-1]
    print(answer)



# for _ in range(N):
#     ls = list(map(int, input().split()))
#     target = [ls[0]]
#     for i in range(1, N):
#         target.append(target[i-1] + ls[i])
#     s_arr.append(target)
#
# for _ in range(M):
#     ans = 0
#     x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())  # x1 <= x2 , y1 <= y2
#     for r in range(x1, x2+1):
#         ans += s_arr[r][y2]
#         if y1 > 0:
#             ans -= s_arr[r][y1-1]
#     print(ans)