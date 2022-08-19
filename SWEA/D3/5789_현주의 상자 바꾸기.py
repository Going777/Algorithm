T = int(input())
for t in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N  # 초기 상태 박스(모두 0)
    for i in range(1, Q + 1):  # Q회 반복
        L, R = map(int, input().split())
        box[L - 1:R] = [i] * (R - L + 1)  # L번째 상자부터 R번쨰 상자까지 i로 치환

    print(f"#{t}", *box)