# 90도씩 회전하는 함수
def rotate(arr):
    result = []     # 최종 회전 후 결과

    # 같은 열에서 밑의 행부터 위로 올라오면서 읽으면 90도 회전한 행이 만들어짐
    for j in range(N):
        tmp = []
        for i in range(N-1, -1, -1):
            tmp.append(arr[i][j])
        result.append(''.join(map(str, tmp)))   # 출력형식을 맞춰주기 위해 한 행을 문자열로 다 붙여서 result에 추가

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotate(arr)        # 90도 회전
    rot_180 = rotate(rot_90)    # 180도 회전
    rot_270 = rotate(rot_180)   # 270도 회전

    concat = list(zip(rot_90, rot_180, rot_270))    # 회전이 끝난 후 모든 결과값을 열방향으로 합침

    print(f"#{tc}")

    for row in concat:          # 출력 형식에 맞추어 출력
        print(' '.join(row))


'''
1
3
1 2 3
4 5 6
7 8 9
'''