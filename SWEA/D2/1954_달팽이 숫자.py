T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 움직일 수 있는 방향 규칙 >> 우->하->좌->상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = 0               # 열 기준
    j = -1              # 행 기준
    k = 0               # 방향 기준
    num = 1             # 기록 숫자
    while num <= N**2:  # 기록 숫자가 칸을 모두 채울때까지 반복
        ni = i + di[k]      # 새로운 열 좌표
        nj = j + dj[k]      # 새로운 행 좌표
        if (0 <= ni < N) and (0 <= nj < N) and (arr[ni][nj] == 0):  # 새로운 좌표가 범위 내에 있으면서 아직 기록 전인 경우
            i = ni; j = nj              # 조건을 만족한다면 새로운 좌표로 기준 위치 변경
            arr[i][j] = num             # 변경된 위치에 숫자 기록
            num += 1                    # 기록할 숫자 +1
        else:
            k = (k+1) % 4               # 현재 방향에서 갈 수 있는 곳을 찾지 못했다면, 방향 전환

    print(f"#{tc}")
    [print(*row) for row in arr]