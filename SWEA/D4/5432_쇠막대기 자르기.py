# T = int(input())
# for t in range(1, T + 1):
#     txt = list(input())
#     lst = []
#     stick_cnt = 0
#     result = 0
#     for i in txt:
#         if i == "(":
#             lst.append(i)
#             stick_cnt += 1
#         else:
#             if lst[-1] == "(":  # 레이저 부분
#                 stick_cnt -= 1
#                 result += stick_cnt
#                 lst.append(i)
#             else:  # 쇠막대기가 끝나는 부분
#                 result += 1
#                 stick_cnt -= 1
#
#     print(f"#{t} {result}")

#-----------------------------------------------------------------------------------------

# 스택 활용
T = int(input())
for t in range(1, T+1):
    txt = list(input())
    stack = []
    result = 0
    for i in txt:
        if i == "(":                    # 여는 괄호라면 스택에 추가
            stack.append(i)
        else:
            stack.pop()                 # 닫는 괄호라면 스택에서 원소 한 개 제거

            if tmp == "(":              # 레이저 부분
                result += len(stack)
            else:                       # 막대가 끝나는 부분
                result += 1
        tmp = i                         # 이전 값을 기억 > 레이저 부분과 막대 끝지점 구분 위해

    print(f"#{t} {result}")