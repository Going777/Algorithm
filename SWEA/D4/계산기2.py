T = 10
for tc in range(1, T+1):
    _ = int(input())
    txt = input()
    eq = ""
    sign = {"*": 2, "+": 1}
    stack = []

    for c in txt:
        if c.isnumeric():
            eq += c
        else:
            while stack and sign[c] <= sign[stack[-1]]:
                eq += stack.pop()
            stack.append(c)
    while stack:
        eq += stack.pop()

    # 후위표기식 처리
    for c in eq:
        if c.isnumeric():
            stack.append(int(c))
        else:
            first = stack.pop()
            second = stack.pop()
            if c == "+":
                stack.append(second + first)
            elif c == "*":
                stack.append(second * first)

    print(f"#{tc} {stack[-1]}")
