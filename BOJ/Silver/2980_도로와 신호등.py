N, L = map(int, input().split())    # N: 신호등 개수 / L: 도로 길이(0부터 시작)
ans = 0
prev_D = 0
for _ in range(N):
    D, R, G = map(int, input().split())     # D: 신호등 위치 / R, G: 빨간불, 초록불 지속 시간

    ans += D-prev_D

    time = [0, 1]
    while True:
        time[0] += R
        time[1] = 1
        if time[0] >= ans:
            break

        time[0] += G
        time[1] = 0
        if time[0] > ans:
            break

    if time[1] == 1:                        # 현재 신호가 빨간불이면
        ans += time[0]-ans                  # 기다려야하는 시간만큼 추가

    prev_D = D                              # 현재 신호등 위치 저장

ans += L - prev_D                           # 현재 위치에서 도착지에 도착할때까지의 거리 추가
print(ans)