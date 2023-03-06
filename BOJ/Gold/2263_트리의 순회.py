# n개의 정점을 갖는 이진트리 (1~N까지 중복X)
# 중위순회 / 후위순회가 적혀있을 때, 전위순회는?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

lst = [0] * (N+1)
# 각 숫자가 중위순회 리스트 내 몇 번째 위치하고 있는지 찾을 수 있도록 세팅
for i in range(N):
    lst[inorder[i]] = i

def order(in_s_idx, in_e_idx, post_s_idx, post_e_idx):
    # 종료 시점 => 각 순회의 시작 인덱스와 끝 인덱스가 교차하게되는 시점
    if ((in_e_idx < in_s_idx) or (post_e_idx < post_s_idx)):
        return

    # 후위 순회의 끝점은 루트 노드
    root = postorder[post_e_idx]
    print(root, end=' ')

    # 중위순회에서 루트 노드의 좌/우로 트리가 나뉘기 때문에 해당 개수 세기
    left_cnt = lst[root] - in_s_idx
    right_cnt = in_e_idx - lst[root]

    order(in_s_idx, in_s_idx + left_cnt - 1, post_s_idx, post_s_idx + left_cnt - 1)     # 왼쪽 서브트리 재귀호출
    order(in_e_idx - right_cnt + 1, in_e_idx, post_e_idx - right_cnt, post_e_idx - 1)   # 오른쪽 서브트리 재귀호출

order(0, N-1, 0, N-1)