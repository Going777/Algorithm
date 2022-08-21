import sys
sys.stdin = open('../D2/input.txt', 'r')


def dfs(v):
    ans = ''
    top = -1

    visited[v] = 1
    ans += f'{v+1} '
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[v] = 1
                ans += f"{v+1} "
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break
    return ans

# 시작 정점은 1부터 시작
# 여러 개의 정점이 있다면 낮은 번호의 정점을 우선적으로 방문
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    N = V
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        x, y = map(int, input().split())
        # 양방향 처리
        adjList[x-1].append(y-1)
        adjList[y-1].append(x-1)

    visited = [0] * N
    stack = [0] * N
    ans = dfs(0) # 시작 정점은 1이지만 인덱스를 맞춰주기 위해 0부터 시작하는 것으로 생각
    print(f"#{t} {ans}")


