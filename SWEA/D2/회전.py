T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    for _ in range(M):
        x = q.pop(0)
        q.append(x)

    print(f"#{tc} {q[0]}")