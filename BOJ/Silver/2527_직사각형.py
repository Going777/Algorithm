def my_max(x, y):
    return x if x > y else y
def my_min(x, y):
    return x if x < y else y

T = 4
for _ in range(T):
    A_x1, A_y1, A_x2, A_y2, B_x1, B_y1, B_x2, B_y2 = map(int, input().strip().split())

    # 겹치는 부분 만들기
    x1 = my_max(A_x1, B_x1)
    x2 = my_min(A_x2, B_x2)
    y1 = my_max(A_y1, B_y1)
    y2 = my_min(A_y2, B_y2)

    # 겹치는 사각형 가로, 세로 길이 구하기
    x_diff = x2 - x1
    y_diff = y2 - y1

    # 직사각형: a / 선분: b / 점: c / 공통부분 없음: d
    if x_diff > 0 and y_diff > 0:  # 길이가 모두 0보다 크다면 겹치는 부분이 만들어진 것
        print('a')
    elif x_diff == 0 and y_diff == 0:  # 길이가 모두 0이라면 꼭지점끼리 만난 것
        print("c")
    elif x_diff < 0 or y_diff < 0:  # 길이가 하나라도 음수가 나오면 겹치는 부분이 없는 것
        print("d")
    else:  # 이외의 경우 선끼리 맞닿은 것
        print("b")
