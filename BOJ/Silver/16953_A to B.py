from collections import deque
import sys
input = sys.stdin.readline

# 메모리초과 되지 않기 위해 visited 배열 없이 구현하는 방법 고안
# q에서 cnt를 함께 넘겨 줌
def bfs(n):
    q = deque()

    q.append([n,1])

    while q:
        i, cnt = q.popleft()
        if i == B:
            return cnt
        for tmp in [i*2, (10*i)+1]:
            if tmp <= B:
                q.append([tmp, cnt+1])
    return -1

A, B = map(int, input().split())
# 할 수 있는 연산
# 1. 2를 곱한다
# 2. 1을 수의 가장 오른쪽에 추가한다

ans = bfs(A)
print(ans)