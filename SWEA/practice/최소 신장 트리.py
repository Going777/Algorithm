'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
가중치 합이 최소가 되도록 만드는 경우를 최소신장트리라고 한다
0~V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
이 그래프로부터 최소 신장트리를 구성하는 간선의 가중치를 모두 더해 출력하라
'''
# PRIM - 노드 중심
def prim(s):
    mst = [0]*(V+1)
    mst[s] = 1
    cnt = 0

    for _ in range(V):    # 포함안된 V 노드개수만큼 처리(총 V+1개 중 출발점 하나는 처리 된 상태)
        mn = INF
        i_mn = 0
        # mst에 포함된 노드를 찾으면, 포함안된 모드 노드와의 최소값 노드 저장
        for s in (V+1):
            if mst[s] == 1: # mst에 포함되어 있으면
                for e in range(V+1):
                    # e가 mst 미포함이고, 더 짧은 경로이면 갱신
                    if mst[e] == 0 and mn>adjA[s][e]:
                        mn = adjA[s][e]
                        i_mn = e
        mst[i_mn] = 1
        cnt += mn
    return cnt

T = int(input())
INF = 10*1000
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjA = [[INF]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s,e,w = map(int, input().split())
        adjA[s][e] = w
        adjA[e][s] = w
    ans = prim(0)
    print(ans)

# KRUSKAL
# def find_set(x):
#     while x != rep[x]:
#         x = rep[x]
#     return x
#
# def union(x, y):
#     rep[find_set(y)] = find_set(x)
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())        # V: 마지막 정점번호 / E: 간선 개수
#     edges = []
#     for _ in range(E):
#         n1, n2, cost = map(int, input().split())
#         edges.append([cost, n1, n2])
#     edges.sort()
#
#     rep = [i for i in range(V+1)]
#     cnt = 0
#     total_cost = 0
#     for cost, n1, n2 in edges:
#         if find_set(n1) != find_set(n2):
#             cnt += 1
#             union(n1, n2)
#             total_cost += cost
#             if cnt == V:
#                 break
#     print(f'#{tc} {total_cost}')

'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''