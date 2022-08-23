import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    _ = int(input())
    txt = input()
    eq = ""                     # 후위표기식
    stack = []                  # 부호 담기
    prior = {"(": 0, "*": 2, "+": 1}    # 부호 우선순위

    # [1] 후위표기식으로 변환
    for c in txt:
        if c.isdigit():                     # 숫자라면 eq에 바로 추가
            eq += c
        elif c == "(":                      # 여는 괄호라면 스택에 추가
            stack.append(c)
        else:                               # 연산자(괄호 포함) 라면
            if c == ")":                    # 연산자 중에서도 닫는 괄호라면
                while True:                 # 스택에 마지막 원소가 여는 괄호가 나올 때까지 pop해서 eq에 추가
                    if stack[-1] == "(":    # 마지막 원소가 여는 괄호라면
                        stack.pop()         # 괄호는 식에서 필요 없으므로 pop
                        break
                    eq += stack.pop()
            else:                           # 괄호가 아닌 연산자라면
                while stack and prior[c] <= prior[stack[-1]]:   # 스택이 비거나 현재 연산자의 우선순위보다 스택의 마지막 원소의 우선순위가 높아질때까지
                    eq += stack.pop()                           # 스택에서 pop하고 eq에 추가
                stack.append(c)                                 # 현재 연산자는 스택에 추가

    while stack:                                                # 스택에 남아있는 모든 연산자
        eq += stack.pop()                                       # eq에 추가

    # [2] 연산 계산
    for c in eq:
        if c.isdigit():                     # 후위표기식 내 원소가 숫자라면
            stack.append(int(c))            # 스택에 추가
        else:                               # 연산자라면
            if stack:                       # 스택이 비지 않았다면 (정상적인 후위표기식이라면 스택이 빈 경우는 없을 것)
                f = stack.pop()             # 스택 맨 위 원소 (연산 순서에서 두 번째로)
                s = stack.pop()             # 스택 위에서 두 번째 원소 (연산 순서에서 첫 번째로)
                if c == "+":
                    stack.append(s + f)     # 연산을 하고 나서 스택에 다시 추가
                elif c == "*":
                    stack.append(s * f)     # 연산을 하고 나서 스택에 다시 추가

    print(f"#{tc} {stack[-1]}")             # 최종적으로 스택에 남은 마지막 원소가 최종 계산 결과

'''
1
1
3+4*2*(5+4)
'''