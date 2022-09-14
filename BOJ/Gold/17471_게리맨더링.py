from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def calc_sm(g):
    q = deque()
    g_check = []        # 연결된 구역 리스트

    q.append(g[0])
    g_check.append(g[0])
    sm = pop[g[0]]

    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if t not in g_check and t in g:     # 아직 체크되지 않은 구역이면서, 그룹(g) 내 구역인 경우
                q.append(t)
                g_check.append(t)
                sm += pop[t]

    if len(g) == len(g_check):  # 모두 연결되었다면, 인구 합 리턴
        return sm
    else:                       # 연결이 안되었다면, 0 리턴
        return 0

N = int(input())    # 구역 개수
pop = [0] + list(map(int, input().split()))   # 1~N번까지의 구역별 인구 수
# 인접리스트 만들기
adjLst = [[] for _ in range(N+1)]
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for n in lst[1:]:
        adjLst[i].append(n)

ans = 123456789  # 초기값
isMin = False
comb_lst = set(range(1, N+1))
for i in range(1, N//2+1):                  # g1과 g2는 서로 배반되므로 절반 개수까지만 검사
    for g1 in combinations(comb_lst, i):
        g2 = comb_lst.difference(g1)        # g1의 차집합이 g2
        g1_p = calc_sm(list(g1))            # g1 인구수 구하기
        g2_p = calc_sm(list(g2))            # g2 인구수 구하기
        # 한 그룹에라도 인구수 0명이 있다면, 구역 나누기 불가능
        if (g1_p == 0 or g2_p == 0):
            if ans == 123456789:            # ans 값이 아직 초기값이라면
                ans = -1                    # ans = -1 (나눌 수 없는 경우)
            else:                           # ans가 초기값이 아니라면
                continue                    # 넘어감
        # 구역 나누기 가능
        else:
            if ans == -1:                   # ans 값이 -1이라면
                ans = abs(g1_p - g2_p)      # 현재 값으로 업데이트
            else:                                   # ans에 유효한 값이 있다면
                ans = min(ans, abs(g1_p - g2_p))    # 최소값으로 업데이트
        if ans == 0:                        # ans = 0이 유효한 인구수 차이로 만들 수 있는 최소값 > 종료
            isMin = True
            break
    if isMin:
        break

print(ans)