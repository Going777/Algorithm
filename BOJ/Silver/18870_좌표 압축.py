# 수직선 위에 N개의 좌표가 있다
# Xi를 좌표 압축한 결과,
# X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다
# X1, X2, ..., XN에 좌표 압축을 적용한 결과인 X'1, X'2, ..., X'N를 출력하라

import sys

N = int(sys.stdin.readline())
lst = list(map(int, input().strip().split()))
result = []

for i in range(N):
    cnt = 0
    tmp = []
    for j in range(N):
        if lst[i] > lst[j] and lst[j] not in tmp:
            tmp.append(lst[j])
            cnt += 1
    result.append(cnt)

print(result)