code_dict = {'0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011',
             '5': '0110001', '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    isFind = False
    code = []
    for row in arr:
        for j in range(len(row)-1, 54, -1):
            if row[j] == '1':
                code = row[j-55:j+1]
                isFind = True
                break
        if isFind:
            break

    code_d = []
    for i in range(0, len(code), 7):
        tmp = code[i:i+7]
        for k, v in code_dict.items():
            if ''.join(tmp) == v:
                code_d.append(int(k))

    even = odd = eq = 0
    for i in range(len(code_d)):
        if i%2 == 0:
            even += code_d[i]
        else:
            odd += code_d[i]
    eq = 3*even+odd
    if eq % 10 == 0:
        eq -= 2*even
    else:
        eq = 0
    print(f'#{tc} {eq}')

'''
2
16 80
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000011101101100010111011011000101100010001101001001101110110000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
11 70
00000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000001100101000110100011010111101101110010011001001101110110000000000
00000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000
'''