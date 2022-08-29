def dfs(s):
    global mx_cnt
    visited = [-1]*N
    stack = []
    cnt = 0

    visited[s] = 0
    # print(s)

    while True:
        for t in adjLst[s]:
            if visited[t] == -1:
                stack.append(s)

                visited[t] = visited[s] + 1
                s = t
                cnt += 1

                # print(s, cnt)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

    print("0", visited)
    if mx_cnt < cnt:
        mx_cnt = cnt

N = int(input())
adjLst = [[] for _ in range(N)]

arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == "Y":
            adjLst[i].append(j)

mx_cnt = 0
for n in range(N):
    dfs(n)
    print()
    print()

print(mx_cnt)