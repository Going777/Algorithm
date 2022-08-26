# def solve():
#     for si in range(N):
#         for sj in range(N):
#             for di, dj in [(0,1),(-1,0),(1,1),(-1,1)]:
#                 for mul in range(5):
#                     ni = si + di*mul
#                     nj = sj + dj*mul
#                     if 0<=ni<N and 0<=nj<N and arr[ni][nj] == "o":
#                         pass
#                     else:
#                         break
#                 else:               # if 문을 5번 모두 통과했다면 5개 돌이 연속으로 존재하는 것
#                     return "YES"
#     return "NO"

def check_row(arr):
    for row in arr:
        if sum(row) == 5:
            return "YES"
    return "NO"

def check_diag(arr):
    diag1_sm = diag2_sm = 0
    for i in range(5):
        if arr[i][i] == 1:
            diag1_sm += 1
        else:
            diag1_sm = 0

        if arr[i][5-i-1] == 1:
            diag2_sm += 1
        else:
            diag2_sm = 0

    if diag2_sm == 5 or diag1_sm == 5:
        return "YES"
    return "NO"

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().replace("o","1").replace(".","0"))) for _ in range(N)]
    isTerminate = False

    for i in range(N - 4):
        for j in range(N - 4):
            tmp = [row[j:j + 5] for row in arr[i:i + 5]]
            ans = check_row(tmp)
            if ans == "YES":
                isTerminate = True
                break
            ans = check_row(list(zip(*tmp)))
            if ans == "YES":
                isTerminate = True
                break
            ans = check_diag(tmp)
            if ans == "YES":
                isTerminate = True
                break
        if isTerminate:
            break

    print(f"#{tc} {ans}")

'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
7
......o
.....o.
....o..
...o...
..o....
.......
.......
'''