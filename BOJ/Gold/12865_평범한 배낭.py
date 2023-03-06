# N개의 물건 존재
# 각 물건은 무게 w와 가치 V를 가짐
# 배낭에 최대 K만큼의 무게만을 넣을 수 있을 때, 물건들의 가치합의 최댓값은?

import sys
input = sys.stdin.readline


# 백트래킹 -> 시간초과 실패

# def dfs(n, smW, smV):
#     global ans
#     if smW > K:
#         return
#
#     if n == N:
#         ans = max(ans, smV)
#         return
#
#     dfs(n+1, smW, smV)                        # 물건 포함X
#     dfs(n+1, smW+lst[n][0], smV+lst[n][1])    # 물건 포함
#
#
# N, K = map(int, input().split())
# lst = []
# ans = 0
# for _ in range(N):
#     lst.append(list(map(int, input().split())))
# dfs(0, 0, 0)
# print(ans)

# DP -> 통과
N, K = map(int, input().split())
table = [0] * (K+1)                 # 가능한 무게 테이블 리스트를 관리

for _ in range(N):
    w, v = map(int, input().split())
    if w > K: continue              # 무게가 기준무게보다 높다면 제외
    # 리스트 뒤쪽에서부터 채움(무게가 많이 나가는 쪽 먼저 계산)
    for i in range(K, 0, -1):
        if table[i] != 0 and i+w <= K:  # 무게를 더했을 때 기준무게 내에 존재하는 경우
            table[i+w] = max(table[i+w], table[i]+v)  # 가치 최댓값으로 업데이트
    table[w] = max(v, table[w])     # 본 무게에 해당하는 물건의 본래 가치값과 지금껏 계산된 가치값 비교 후, 최댓값으로 업데이트
print(max(table))



