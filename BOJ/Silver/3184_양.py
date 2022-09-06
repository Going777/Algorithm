from collections import deque
di = [-1,1,0,0] ; dj = [0,0,-1,1]
def bfs(i, j):
    q = deque()
    tmp_s = tmp_w = 0

    if arr[i][j] == "o":
        tmp_s += 1
    elif arr[i][j] == "v":
        tmp_w += 1
    q.append([i, j])
    visited[i][j] = 1
    arr[i][j] = 1           # 방문하고 나서는 더이상 탐색하지 못하도록 다른 문자로 치환

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k] ; nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != "#":
                if arr[ni][nj] == "o":
                    tmp_s += 1
                elif arr[ni][nj] == "v":
                    tmp_w += 1
                q.append([ni, nj])
                visited[ni][nj] = 1
                arr[ni][nj] = 1     # 방문하고 나서는 더이상 탐색하지 못하도록 다른 문자로 치환

    if tmp_s > tmp_w:   # 양이 늑대보다 많으면 늑대 수는 0
        tmp_w = 0
    else:               # 늑대가 양보다 많거나 같으면 양의 수는 0
        tmp_s = 0

    return [tmp_s, tmp_w]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
s = w = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] in [".", "v", "o"]:
            tmp_s, tmp_w = bfs(i, j)
            s += tmp_s
            w += tmp_w

print(s, w)

'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
'''