# 잘린 비트만큼 10진수로 바꾸기
def solve(lst):
    ans = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            ans += 2**i
    return ans

# 16진수 -> 2진수로 바꾸기
def hex_to_bin(n):
    ans = [0]*4
    for i in range(3,-1,-1):
        ans[i] = n % 2
        n //= 2
    return ans

# A~F 숫자로 매핑하는 딕셔너리 만들기
keys = []
for c in range(65, 71):
    keys.append(chr(c))
values = list(range(10, 16))
hex_dict = dict(zip(keys, values))

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    bin_lst = []
    for n in lst:
        if n in hex_dict.keys():
            n = hex_dict[n]
        else:
            n = int(n)
        bin_lst.extend(hex_to_bin(n))

    result = []
    for i in range(0, len(bin_lst), 7):
        tmp = bin_lst[i:i+7]
        result.append(solve(tmp[::-1]))
    print(f'#{tc}', end=' ')
    print(*result, end='\n')


'''
3
0F97A3
6079861D79F
01D06079861D79F99F
'''