import sys
input = sys.stdin.readline

# 삭제할 노드 및 자식 노드들에 대해 -2로 처리
def dfs(n):
    arr[n] = -2
    for i in range(N):
        if n == arr[i]:
            dfs(i)

N = int(input())    # 노드 개수(N <= 50)
arr = list(map(int, input().split()))  # 각 노드의 부모노드 표시
target = int(input())   # 지울 노드

dfs(target)

cnt = 0
# 리프 노드 찾기(삭제된 노드(=-2)가 아니면서, 부모 노드가 아닌 경우)
for i in range(N):
    if arr[i] != -2 and i not in arr:
        cnt += 1
print(cnt)

