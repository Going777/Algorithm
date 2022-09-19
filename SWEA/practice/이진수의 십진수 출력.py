def solve(lst):
    ans = 0
    for i in range(len(lst)):
        if lst[::-1][i] == 1:
           ans += 2**i
    return ans

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    result = []
    for i in range(0, len(lst), 7):
        tmp = lst[i:i+7]
        result.append(solve(tmp))
    print(f'#{tc}', end=' ')
    print(*result, end='\n')

'''
3
0000111100000000001110000011
111111100000001000100000011101010101100110
0000000111100000011000000111100110000110000111100111100111111001100111
'''