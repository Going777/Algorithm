T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    station.append(N)                           # 마지막 도착 정류장 추가
    result = 0

    start = prev = 0            # 출발지점 0으로 초기화
    for nxt in station:
        if nxt - prev > K:      # 충전기 간 거리가 K보다 크다면 자동차가 다음 충전소까지 갈 수 없는 것 > 종료
            result = 0
            break
        # 충전기까지의 거리는 확보된 상태 > 현재 위치를 옮겨야 함
        if nxt - start > K:     # 현재 위치에서 충전기까지의 거리가 K보다 커진다면
            start = prev        # 현재 위치를 이전 충전소 위치로 옮겨야함
            result += 1         # 위치를 옮겼으므로 result + 1
        prev = nxt              # 사이클을 돌때마다 다음 충전소 위치를 이전 충전소 위치로 저장

    print(f"#{tc} {result}")