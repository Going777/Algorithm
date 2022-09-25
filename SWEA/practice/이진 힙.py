# 이진 최소힙
def enq(n):
    global last
    # 제일 마지막에 추가
    last += 1
    heap[last] = n

    c = last
    p = c // 2
    # 부모가 존재하고, 부모가 나보다 큰 경우: 교환!!
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    last = 0
    for n in list(map(int, input().split())):
        enq(n)

    ans = 0
    c = N
    p = c // 2
    # 조상노드들의 합 구하기
    while p > 0:    # 부모가 존재하는 경우(조상 존재)
        ans += heap[p]
        c = p
        p = c // 2

    print(f'#{tc} {ans}')

'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''