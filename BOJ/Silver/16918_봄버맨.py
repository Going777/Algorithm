from collections import deque

di = [-1,1,0,0]; dj = [0,0,-1,1]
def solve(bomb):
    q = deque()

    arr = [row[:] for row in all_arr]   # 모든 칸을 폭탄으로 초기화하고 시작

    # 저장된 폭탄위치를 기반으로 상하좌우 폭탄 없음으로 change
    for i, j in bomb:
        q.append([i,j])
        arr[i][j] = '.'

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + di[k]; nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                arr[ni][nj] = '.'

    return arr

R, C, N = map(int, input().split()) # R: 행 수 / C: 열 수 / N: 시간(N초 후 결과 확인)
base_arr = [list(input()) for _ in range(R)]   # 빈 칸은 '.' 폭탄은 'o'로 표시
all_arr = [['O']*C for _ in range(R)]

bomb1 = []
for i in range(R):
    for j in range(C):
        if base_arr[i][j] == 'O':
            bomb1.append([i, j])    # 폭탄 위치 기록
bomb1_arr = solve(bomb1)            # 첫 번째 폭탄 터진 상태

bomb2 = []
for i in range(R):
    for j in range(C):
        if bomb1_arr[i][j] == 'O':
            bomb2.append([i, j])    # 폭탄 위치 기록
bomb2_arr = solve(bomb2)            # 두 번째 폭탄 터진 상태

# 상태는 총 4가지로 구분됨!
if N <= 1:
    [print(''.join(row)) for row in base_arr]
elif N % 2 == 0:
    [print(''.join(row)) for row in all_arr]
elif N%4 == 3:
    [print(''.join(row)) for row in bomb1_arr]
else:
    [print(''.join(row)) for row in bomb2_arr]

'''
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....
'''