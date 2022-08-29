T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 노선 수
    counts = [0] * 1001     # 각 정류장 노선 카운트 배열

    for _ in range(N):
        t, A, B = map(int, input().split()) # t: 버스 종류 / A: 출발 정류장 / B: 도착 정류장
        # 일반정류장은 모든 정류장 정차
        if t == 1:
            for n in range(A, B+1):
                counts[n] += 1
        # 급행 정류장은 A가 짝수면, 짝수 정류장 정차 / 홀수면 홀수 정류장 정차
        elif t == 2:
            for n in range(A, B, 2):
                counts[n] += 1
            counts[B] += 1
        # 광속 급행 정류장은 A가 짝수면 4의 배수 정류장 정차 / 홀수면 3의 배수지만 10의 배수는 아닌 정류장 정차
        if t == 3:
            counts[A] += 1
            if A % 2 == 0:  # A가 짝수
                for n in range(4, B, 4):
                    if A < n:
                        counts[n] += 1
            else:           # A가 홀수
                for n in range(3, B, 3):
                    if A < n and n % 10 != 0:
                        counts[n] += 1
            counts[B] += 1

    ans = max(counts)
    print(f"#{tc} {ans}")

'''
1
3
1 2 5
2 3 10
3 2 9
'''