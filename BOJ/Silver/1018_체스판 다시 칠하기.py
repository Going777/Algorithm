'''
NxM 크기의 보드판은 어떤 정사각형은 검은색으로 칠해져있고, 나머지는 흰색으로 칠해져있다
이 보드를 잘라서 8x8 크기의 체스판을 만들려고 한다
체스판은 검은색/흰색이 번갈아 칠해져 있어야 한다
체스판을 칠하는 경우는 2가지 - 맨 왼쪽 위칸이 흰색 or 검은색
'''

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
mn = 64
for i in range(N-7):
    for j in range(M-7):
        start_b = 0         # 시작점이 검은색 때 바꿔야할 개수
        start_w = 0         # 시작점이 흰색일 때 바꿔야할 개수
        # 8x8 크기 내 원소 검사
        for ii in range(i, i+8):
            for jj in range(j, j+8):
                if (ii + jj) % 2 == 0:
                    if arr[ii][jj] != 'B':
                        start_b += 1
                    elif arr[ii][jj] != 'W':
                        start_w += 1
                else:
                    if arr[ii][jj] != 'W':
                        start_b += 1
                    elif arr[ii][jj] != 'B':
                        start_w += 1
        mn = min(mn, start_b, start_w)      # 최소값 갱신
print(mn)