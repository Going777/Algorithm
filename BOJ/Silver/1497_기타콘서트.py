'''
최대한 많은 곡을 연주하려고 할 때, 필요한 기타의 최소 개수는?
'''
from itertools import combinations

N, M = map(int, input().split())    # N: 기타 개수 / M: 곡 개수
ans = -1
musics = []
# 기타 이름 / 기타 연주할 수 있는 곡 정보(Y: 연주 가능, N: 연주 불가능)
for _ in range(N):
    _, m = list(input().split())
    m = int(m.replace("Y","1").replace("N", "0"), 2)
    musics.append(m)

ans = 0
mn_cnt = N
for n in range(1, N+1):
    for com in combinations(range(0, N), n):
        tmp = 0
        cnt = len(com)
        for c in com:
            tmp = tmp | musics[c]
        print(com, tmp)
        if tmp >= ans and mn_cnt > cnt:
            mn_cnt = cnt
            ans = tmp

if not ans:
    mn_cnt = -1
print(mn_cnt, ans)

'''
4 5
GIBSON YYYNN
FENDER YYNNY
EPIPHONE NNNYY
ESP YNNNN
'''

'''
4 8 16 > 28
1 8 16 > 25
1 2 > 3
16 > 16
'''
