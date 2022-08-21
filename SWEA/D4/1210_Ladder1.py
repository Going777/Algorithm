T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    t_arr = []
    t_arr = [row for row in arr[::-1]] # 상하반전
    # 시작점 찾기
    s = 0
    for idx in range(N):
        if t_arr[0][idx] == 2:
            s = idx
            break

    i = 0                                           # 시작점 초기화 (행)
    j = s                                           # 시작점 초기화 (열)
    while True:
        t_arr[i][j] = 2                             # 현재 위치 표시
        if i == N-1:                                # 마지막 행까지 모두 탐색했다면 종료
            break
        for k in [-1, 1]:                           # 좌우로 갈 수 있는지 검사
            nj = j + k                              # 새로운 열 좌표
            if 0 <= nj < N and t_arr[i][nj] == 1:   # 새로운 열 좌표가 범위내에 있으면서, 갈 수 있는 곳이라면
                j = nj                              # 열 좌표 업데이트
                break
        else:                                       # 좌우로 갈 수 없다면
            i += 1                                  # 밑으로 이동 (행 +1)

    print(f"#{tc} {j}")