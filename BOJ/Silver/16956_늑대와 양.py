R, C = map(int, input().split())    # R: 행 개수 / C: 열 개수
# '.'는 빈 칸, 's'는 양, 'w'는 늑대
arr = [list(input()) for _ in range(R)]

di = [-1,1,0,0] ; dj = [0,0,-1,1]
catch = False
for i in range(R):
    for j in range(C):
        # 늑대라면 상하좌우 검사 후, 양이 있으면 catch를 True로 바꾸고 반복문 종료
        if arr[i][j] == "W":
            for k in range(4):
                ni = i + di[k] ; nj = j + dj[k]
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == "S":
                    catch = True
                    break
        # 빈 칸이라면 벽으로 바꿈 (벽의 개수는 상관이 없기 때문에)
        elif arr[i][j] == '.':
            arr[i][j] = "D"
    if catch:
        break

if catch:
    print(0)
else:
    print(1)
    [print(''.join(row)) for row in arr]

'''
6 6
..S...
..S.W.
.S....
..W...
...W..
......
'''