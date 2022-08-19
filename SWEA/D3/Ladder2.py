import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

def copy_arr(arr):
    copy_arr = []
    for lst in arr:
        row = lst[:]
        copy_arr.append(row)
    return copy_arr

T = 10
for _ in range(T):
    t = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    start_idx = []
    # arr의 첫 행에서 출발 가능 지점 찾기 (값이 1인 경우)
    for idx in range(N):
        if arr[0][idx] == 1:
            start_idx.append(idx)

    min_cnt = N*N                   # 최소 거리
    result = 0                      # 최소 거리에 해당하는 출발점 x좌표

    for s in start_idx:
        i = 0       # 열
        j = s       # 행
        tmp = 0     # 각 출발지점에서의 거리
        arr_tmp = copy_arr(arr)     # 출발지점에 새롭게 시작할 때마다 사다리 리셋
        while True:
            arr_tmp[i][j] = 2       # 지나온 길 표시
            tmp += 1                # 거리 += 1
            if i == N-1:            # 마지막 행에 도달했다면 종료
                break
            for k in [-1, 1]:       # 좌우로 갈 수 있는지 검사
                nj = j + k
                if 0 <= nj < N and arr_tmp[i][nj] == 1:
                    j = nj          # 갈 수 있다면 열 인덱스 변경
                    break
            else:
                 i += 1             # 좌우로 갈 수 없다면 다음 행으로 이동
        if min_cnt >= tmp:          # 최소 거리 찾기 (같은 거리면 높은 좌표가 정답)
            min_cnt = tmp
            result = s

    print(f"#{t} {result}")