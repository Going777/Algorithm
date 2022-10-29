'''
최대한 많은 곡을 연주하려고 할 때, 필요한 기타의 최소 개수는?
'''
from itertools import combinations

N, M = map(int, input().split())    # N: 기타 개수 / M: 곡 개수
musics = []
# 기타 이름 / 기타 연주할 수 있는 곡 정보(Y: 연주 가능, N: 연주 불가능)
for _ in range(N):
    _, m = list(input().split())
    m = int(m.replace("Y","1").replace("N", "0"), 2)    # Y(1), N(0)으로 교체 > int형 > 2진수로 변환
    musics.append(m)

mx_songs = 0        # 최대 연주할 수 있는 노래 수
mn_cnt = N          # 최소 필요한 기타 수
for n in range(1, N+1):
    for com in combinations(range(0, N), n):
        tmp = 0
        cnt = len(com)
        for c in com:
            tmp = tmp | musics[c]
        if tmp > mx_songs:
            mx_songs = tmp
            mn_cnt = cnt

if not mx_songs:
    mn_cnt = -1
print(mn_cnt)

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
