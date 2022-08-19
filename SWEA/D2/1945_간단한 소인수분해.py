T = int(input())
for t in range(1, T + 1):
    num = int(input())
    div = [2, 3, 5, 7, 11]  # 약수 배열
    result = []

    for d in div:
        cnt = 0
        while (num % d == 0):  # 해당 약수로 나누어떨어지면 계속 반복
            cnt += 1  # 카운트 +1
            num //= d  # 타겟값인 num은 약수로 나눠줌
        result.append(cnt)

    print(f"#{t}", *result)