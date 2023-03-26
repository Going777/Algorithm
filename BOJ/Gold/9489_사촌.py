# [트리 정의 규칙]
    # 첫 번째 정수는 트리의 루트 노드
    # 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타냄
        # (이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1 보다 크다)
    # 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 됨
        # ( 노드가 여러가지라면 가장 작은 수를 갖는 노드의 자식이 된다)
    # 집합은 수가 연속하지 않는 곳에서 구분됨

# 두 노드의 부모는 다르지만, 두 보모가 형제일 때 두 노드를 사촌이라 함
# k의 사촌의 수는?

import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())

    # 종료
    if n == 0:
        break

    ans = 0
    # 위치 찾기 편하게 하기 위해 맨 앞에 임의의 수 추가
    nodes = [-2] + list(map(int, input().split()))
    parents = [0] * (n+1)
    parents[0] = -2

    target = 0
    num = -1    # 부모 노드값으로 매핑될 값

    for i in range(1, n+1):
        # 타겟값의 위치 찾기
        if nodes[i] == k:
            target = i

        # 연속된 수가 아니면 부모노드값 + 1
        if nodes[i] != nodes[i-1] + 1:
            num += 1

        # parents 노드 리스트에 매핑
        parents[i] = num

    # 사촌 찾기 (부모 노드는 다르면서, 부모 노드의 부모 노드는 같은 경우)
    for i in range(1, n+1):
        if parents[i] != parents[target] and parents[parents[i]] == parents[parents[target]]:
            ans += 1
    print(ans)