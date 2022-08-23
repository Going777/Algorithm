def calc(sign):
    if sign == "+":
        return s + f
    elif sign == "-":
        return s - f
    elif sign == "*":
        return s * f
    else:
        return s // f

T = int(input())
for tc in range(1, T+1):
    eq = list(input().split())
    stack = []
    isForth = True

    for c in eq:
        if c == ".":                                        # 마침표를 스택의 마지막 값이 연산 결과
            ans = stack.pop()
        elif c.isnumeric():                                 # 숫자면 스택에 추가
            stack.append(int(c))
        else:                                               # 연산자이면
            try:                                            # 스택 내 2개의 원소를 꺼내서 연산
                f = stack.pop()
                s = stack.pop()
                stack.append(calc(c))                       # 연산 후 스택에 추가
            except:                                         # 스택에 원소 2개가 없다면
                ans = "error"                               # 연산 불가능
                break

    if stack:                                               # 스택에 값이 남아있는 경우 연산 불가능
        ans = "error"
    print(f"#{tc} {ans}")