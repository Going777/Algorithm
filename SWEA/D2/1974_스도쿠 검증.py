import sys
sys.stdin = open('input.txt', 'r')

# 스도쿠 검증
def is_sdoku(arr, N):
    # 행/열 두 번 탐색
    for _ in range(2):
        for i in range(N):
            counts = [0] * N # 0~9까지 카운트 저장
            for j in range(N):
                if counts[arr[i][j]-1] != 0: # 이전에 카운트된 숫자가 있다면
                    return 0 # 중복이 있는 것 -> 스도쿠 X(return 0)
                else:
                    counts[arr[i][j]-1] = 1 # 해당 원소에 카운트 + 1
        arr = list(map(list, zip(*arr))) # 행렬 전치 > 열방향을 행으로 바꿔 탐색

    # 3*3 박스 탐색
    for i in range(0, N-3, 3):
        for j in range(0, N-3, 3):
            counts = [0] * N
            for k in range(3):
                for l in range(3):
                    if counts[arr[i+k][j+l]-1] != 0:
                        return 0
                    else:
                        counts[arr[i+k][j+l]-1] = 1

    return 1 # 모든 조건을 통과한 경우 -> 스도쿠 O(return 1)

T = int(input())
for t in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)] # 9 X 9 스도쿠 배열
    result = is_sdoku(arr, N)
    print(f"#{t} {result}")