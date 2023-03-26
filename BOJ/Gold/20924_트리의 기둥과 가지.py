# 기가 노드는 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 2개 이상인 노드
# 트리의 기둥은 루트노드 ~ 기가노드
# 트리의 가지는 기가노드 ~ 임의의 리프노드
# 트리의 기둥과 가장 긴 가지의 길이를 측정하라

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R = map(int, input().split())
adjLst = [[] for _ in range(N+1)]

def dfs(node, prev_node, sm, isBranch):
    # 기둥이라면 기둥의 합 갱신
    if not isBranch:
        ans[0] = sm
    # 가지라면 긴 가지의 합으로 갱신
    else:
        ans[1] = max(ans[1], sm)

    # 루트노드 아닌 경우, 인접한 노드가 2개보다 많으면 기가노드 => 여기부터 가지로 transfer
    # 루트노드인 경우, 인접한 노드가 1개보다 많으면 기가노드
    if not isBranch and ((len(adjLst[node]) > 2) or (node == R and len(adjLst[node]) > 1)):
        isBranch = True
        sm = 0

    for v, d in adjLst[node]:
        # 이미 방문한 노드는 탐색X
        if v == prev_node: continue
        dfs(v, node, sm+d, isBranch)


for _ in range(N-1):
    a, b, d = map(int, input().split())
    adjLst[a].append((b, d))
    adjLst[b].append((a, d))
ans = [0,0]

dfs(R,R, 0, False)
print(*ans)