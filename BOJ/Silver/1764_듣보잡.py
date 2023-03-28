# 듣보잡의 수와 그 명단을 사전 순으로 출력하라

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 듣도 못한 사람의 수 / M: 보도 못한 사람의 수
set_A, set_B = set(), set()
for _ in range(N):
    set_A.add(input().strip())
for _ in range(M):
    set_B.add(input().strip())

result = sorted(set_A.intersection(set_B))
print(len(result))
[print(x) for x in result]