# import sys
# sys.stdin = open('input.txt','r')
code_dict = {'211':0, '221':1, '122':2, '411':3, '132':4, '231':5,
             '114':6, '312':7, '213':8, '112':9}
def solve():
    codes = []
    result = []
    # 행별로 0과 1을 카운트하는 cnts 배열 만들기
    for row in n_arr:
        cnts = []
        old = 0
        if sum(row) == 0:
            continue
        for i in range(len(row)):
            if row[old] != row[i]:
                cnts.append(i-old)
                old = i

        # cnts 배열을 바탕으로 code_dict와 비교해가며 암호 해독하여 codes 배열에 추가
        tmp = []
        for i in range(1, len(cnts), 4):
            a, b, c = cnts[i:i+3]
            mn = min(a, b, c)
            while mn != 1:
                if a%mn == 0 and b%mn == 0 and c%mn == 0:
                    a//=mn ; b//=mn ; c//=mn
                    mn = min(a, b, c)
                else: break
            tmp.append(code_dict[str(a)+str(b)+str(c)])
            if len(tmp) == 8:
                if tmp not in codes:
                    codes.append(tmp)
                tmp = []

    # codes배열 내 암호코드 검증하기
    for code in codes:
        even = odd = 0
        for i in range(len(code)):
            if i % 2:
                odd += code[i]
            else:
                even += code[i]
        if (even*3+odd) % 10:
            result.append(0)
        else:
            result.append(even+odd)
    return result

def hex_to_bin(n):
    b = [0]*4
    for i in range(3, -1, -1):
        b[i] = n % 2
        n //= 2
    return b

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    arr = [list(input()) for _ in range(N)]

    # 16진수를 2진수로 바꾼 n_arr 만들기

    n_arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if '0' <= arr[i][j] <= '9':
                n_arr[i].extend(hex_to_bin(int(arr[i][j])))
            else:
                n_arr[i].extend(hex_to_bin(ord(arr[i][j])-ord('A')+10))

    print(f'#{tc} {sum(solve())}')

'''
2
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000
18 50
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
000000000000000000000000000196EBC5A316C57800000000
00000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
'''