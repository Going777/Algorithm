# 이진 최소힙
def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2

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
    while p > 0:
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