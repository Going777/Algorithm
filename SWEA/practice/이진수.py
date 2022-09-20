def solve(n):
    ans = [0]*4
    for i in range(3, -1, -1):
        ans[i] = str(n % 2)
        n //= 2
    return ''.join(ans)

# 16진수 1자리는 2진수 4자리로 표시됨
T = int(input())
for tc in range(1, T+1):
    N, lst = input().split()
    bin = ''
    for n in lst:
        if n.isdigit():
            bin += solve(int(n))
        else:
            bin += solve(ord(n)-ord('A')+10)
    print(f'#{tc} {bin}')

'''
3
4 47FE
5 79E12
8 41DA16CD
'''