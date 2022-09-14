# import sys
# input = sys.stdin.readline
#
# def bfs(i, j):
#     global ans
#     q = set()
#
#     q.add((i, j, arr[i][j]))
#
#     while q:
#         i, j, alphas = q.pop()
#         ans = max(ans, len(alphas))
#
#         for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#             ni = i + di ; nj = j + dj
#             if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] not in alphas:
#                 q.add((ni, nj, alphas+arr[ni][nj]))
#     return ans
#
# N, M = map(int, input().split())
# arr = [list(input().rstrip()) for _ in range(N)]
# ans = 0
# bfs(0,0)
# print(ans)

# 최대힙
# 삽입
def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last        # 자식 정점 번호
    p = c // 2      # 완전 이진트리에서 부모 정점 번호

    # 부모가 있고, 부모 < 자식인 경우 자리 교환 (부모가 없거나 / 부모 > 자식 조건을 만족할 때까지)
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

# 삭제
def deq():
    global last
    tmp = heap[1]                               # 루트 백업
    heap[1] = heap[last]                        # 삭제할 노드의 키를 루트에 복사
    last -= 1                                   # 마지막 노드 삭제
    p = 1                                       # 루트에 옮긴 값을 자식과 비교
    c = p*2                                     # 왼쪽 자식을 기준으로 시작
    while c <= last:                            # 자식이 하나라도 있으면
        # 오른쪽 자식도 있고, 오른족 자식이 더 크면
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1                              # 비교 대상을 오른쪽 자식으로 변경
        if heap[p] < heap[c]:                   # 자식이 더 크면 최대힙 규칙에 어긋나므로 스왑
            heap[p], heap[c] = heap[c], heap[p]
            p = c                               # 자식을 새로운 부모로
            c = p * 2                           # 새로운 부모의 왼쪽 자식 번호를 계산
        else:                                   # 부모가 더 크면
            break                               # 비교 중단
    return tmp


heap = [0]*7
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

while last:
    print(deq())