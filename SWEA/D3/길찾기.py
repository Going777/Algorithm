import sys
sys.stdin = open('input.txt', 'r')

def dfs(s, e):
    visited[s] = 1
    while True:
        for x in adjLst[s]:
            if not visited[x]:
                if x == e:
                    return 1
                stack.append(s)
                s = x
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                return 0

T = 10
for _ in range(T):
    t, N = map(int, input().split())
    s, e = 0, 99
    size = 100
    adjLst = [[] for _ in range(size)]
    lst = list(map(int, input().split()))
    for idx in range(0, N*2, 2):
        adjLst[lst[idx]].append(lst[idx+1])
    visited = [0] * size
    stack = []

    result = dfs(s, e)

    print(f"#{t} {result}")