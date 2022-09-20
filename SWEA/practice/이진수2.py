T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    while N:
        ans += str(int(N*2))
        if len(ans) >= 13:
            ans = 'overflow'
            break
        N = N*2-int(N*2)
    print(f'#{tc} {ans}')

'''
3
0.625
0.1
0.125
'''