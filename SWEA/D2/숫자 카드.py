T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    counts = [0]*10

    for n in nums:
        counts[n] += 1

    mx_idx = 0
    for i in range(1, 10):
        if counts[mx_idx] <= counts[i]:
            mx_idx = i

    print(f"#{tc} {mx_idx} {counts[mx_idx]}")

