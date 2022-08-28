N = int(input())    # 스위치 개수
bolb = list(map(int, input().split()))  # 전구 상태
M = int(input())    # 학생 수
for _ in range(M):
    g, n = map(int, input().split())    # 성별(남-1, 여-2), 스위치 위치
    # 할당받은 스위치 위치부터 배수 위치마다 스위치 변경
    if g == 1:
        for idx in range(n-1, N, n):
            bolb[idx] = 1 if bolb[idx] == 0 else 0
    # 할당받은 스위치 위치로부터 좌우를 비교하여 같으면 스위치 변경하고, 다르면 중단
    else:
        bolb[n-1] = 1 if bolb[n-1] == 0 else 0  # 자기자신 위치는 기본적으로 변경

        for idx in range(1, N//2+1):
            if n-1-idx < 0 or n-1+idx >= N:     # 범위를 벗어낫다면 종료
                break
            if bolb[n-1-idx] == bolb[n-1+idx]:  # 좌우가 같다면 스위치 변경
                bolb[n-1-idx] = bolb[n-1+idx] = 1 if bolb[n-1-idx] == 0 else 0
            else:   # 같지 않다면 종료
                break

# 출력형식 주의! (20개씩 출력하고 다음줄로)
for idx in range(0, N, 20):
    print(*bolb[idx:idx+20])

'''
64
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
2
1 3
2 4
'''
