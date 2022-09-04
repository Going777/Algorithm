di = [-1,0,1,0]; dj = [0,-1,0,1]
def solve(i, j):
    prev = ''
    k = 0
    cnt = 0
    while True:
        if cnt >= 4 and mat[i][j] != "?":
            break

        ni = i + di[k]; nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if mat[ni][nj] == mat[i][j]:
                return False
            if prev == '':
                if mat[ni][nj] == "?":
                    k = (k+1) % 4
                    continue
                prev = mat[ni][nj]
                mat[i][j] = "#" if prev == "." else "."
            elif mat[ni][nj] != "?" and mat[ni][nj] != prev:
                return False
            mat[ni][nj] = prev
        k = (k+1) % 4
        cnt += 1
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 행 수 / M: 열 수
    mat = [list(input()) for _ in range(N)]     # '#'이면 검은색, '.'이면 흰색, '?'이면 모두 가능
    is_stop = False

    for i in range(N):
        for j in range(M):
            go = solve(i, j)
            if not go:
                is_stop = True
                break
        if is_stop:
            break

    if is_stop:
        print(f"#{tc} impossible")
    else:
        print(f"#{tc} possible")

'''
3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.
'''





