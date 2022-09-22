def to_decimal(lst, m):
    ans = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i]:
           ans += lst[i] * m**i
    return ans

def solve(target, N, m):
    result = []
    for i in range(N):
        for j in range(m):
            tmp = target[i]
            if tmp != j:
                target[i] = j
                result.append(to_decimal(target[::-1], m))
                target[i] = tmp
    return result

T = int(input())
for tc in range(1, T+1):
    bin = list(map(int, input()))     # 2진수
    ter = list(map(int, input()))     # 3진수
    N1 = len(bin) ; N2 = len(ter)
    b = solve(bin, N1, 2)
    t = solve(ter, N2, 3)

    isFind = False
    for b_v in b:
        for t_v in t:
            if b_v == t_v:
                ans = b_v
                isFind = True
        if isFind:
            break

    print(f'#{tc} {ans}')

'''
1
1010
212
'''