# 슬라이딩 윈도우 알고리즘
S, P = map(int, input().split())
dna = input()
table = str.maketrans('ACGT','0123')        # 한 번에 문자 여러개 바꾸기(A>0, C>1, G>2, T>3)
dna = dna.translate(table)
mn_dna = list(map(int, input().split()))    # A, C, G, T 최소 개수
cnt = 0

tmp = [0,0,0,0]
for i in range(P):
    tmp[int(dna[i])] += 1
for k in range(4):
    if tmp[k] < mn_dna[k]:
        break
else:
    cnt += 1

for i in range(P, S):
    r = int(dna[i])
    l = int(dna[i-P])
    tmp[r] += 1
    tmp[l] -= 1
    for k in range(4):
        if tmp[k] < mn_dna[k]:
            break
    else:
        cnt += 1


print(cnt)
'''
9 8
CCTGGATTG
2 0 1 1
'''