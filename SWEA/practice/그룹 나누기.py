'''
수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 적어 제출했다
한 조에 인원을 두지 않았따 >> 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조
번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성한다
1~N번까지의 출석번호가 있고, M장의 신청서가 제출되었다
전체 몇 개의 조가 만들어지는가?
'''
from collections import deque
def find_idx():
    for i in range(1, N+1):
        if visited[i] == 0:
            return i
    return None

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjLst = [[] for _ in range(N+1)]
    input_ = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        adjLst[input_[i]].append(input_[i+1])
        adjLst[input_[i+1]].append(input_[i])
    visited = [0] * (N + 1)
    visited[0] = 1
    ans = 0
    while True:
        n = find_idx()
        if n is None:
            break
        bfs(n)
        ans += 1
    print(f'#{tc} {ans}')

'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''