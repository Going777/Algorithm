'''
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상이 있다
같은 숫자의 점들이 한 곳에 많이 몰려 있으면, 쿼드트리에서는 이를 압축하여 간단히 표현할 수 있다

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 0
모두 1로만 되어 있으면 압축 결과는 1
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지 못하고,
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 이렇게 4개의 영상으로 압축하게 되며
이 4개의 영역을 압축한 결과를 차례로 괄호 안에 묶어서 표현한다
'''
def solve(n, x, y):
    check = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                result.append('(')
                solve(n//2, x, y)
                solve(n//2, x, y+n//2)
                solve(n//2, x+n//2, y)
                solve(n//2, x+n//2, y+n//2)
                result.append(')')
    if check==1:
        result.append('1')
        return
    elif check==0:
        result.append('0')
        return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result = []
solve(N,0,0)
print(''.join(result))


'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''