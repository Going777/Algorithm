N = int(input())

s = 0
e = 1
ans = 1
tmp = 1
while True:
    if s == e == N:
        break
    # 타겟값과 동일하면 start, end 포인트 모두 우측으로 이동
    if tmp == N:
        ans += 1
        e += 1
        tmp += e
        tmp -= s
        s += 1
    # 타겟 숫자보다 작으면 end 포인트를 우측으로 이동
    elif tmp < N:
        e += 1
        tmp += e
    # 타겟 숫자보다 크면 start 포인트를 우측으로 이동
    else:
        tmp -= s
        s += 1

print(ans)