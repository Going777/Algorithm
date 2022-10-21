'''
K개의 랜선을 가지고 있다 (랜선의 길이는 제각각)
랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶다 -> K개의 랜선을 잘라야 한다
만들 수 있는 최대 랜선 길이는?
'''

K, N = map(int, input().split())    # K: 가지고 있는 랜선 개수 / N: 필요한 랜선 개수
lst = []
for _ in range(K):
    lst.append(int(input()))

l = 1
r = max(lst)
while l <= r:
    m = (l + r) // 2
    tmp = 0
    for n in lst:
        tmp += n // m

    if tmp >= N:
        l = m + 1
    else:
        r = m - 1

print(r)

'''
4 11
802
743
457
539
'''