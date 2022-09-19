def hex_to_bin(h):
    bin = [0]*4
    for i in range(3, -1, -1):
        bin[i] = str(h % 2)
        h //= 2
    return bin

pw_dict = {'0': '001101', '1': '010011', '2': '111011', '3': '110001', '4': '100011',
           '5': '110111', '6': '001011', '7': '111101', '8': '011001', '9': '101111'}
T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    bin = []
    for h in lst:
        if h.isdigit():
            bin.extend(hex_to_bin(int(h)))
        else:
            bin.extend(hex_to_bin(ord(h)-ord('A')+10))

    result = []
    i = 0
    while i <= len(bin)-6:
        tmp = bin[i:i+6]
        for k, v in pw_dict.items():
            if ''.join(tmp) == v:
                result.append(k)
                i += 6
                break
        else:
            i += 1

    print(f'#{tc}', end=' ')
    print(*result, end='\n')
'''
2
0DEC
0269FAC9A0
'''