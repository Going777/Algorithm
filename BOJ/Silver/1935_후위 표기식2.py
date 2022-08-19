import sys

N = int(sys.stdin.readline())
eq = input()
stack = []
num = 65    # ASCII에서 A의 코드 값
result = 0
for _ in range(N):
    eq = eq.replace(chr(num), input())
    num += 1

signs = "+-*/"                                  # 부호 모음
for idx in range(len(eq)):
    if eq[idx].isnumeric():                    # 부호가 아닌 숫자라면
        stack.append(int(eq[idx]))              # 스택에 추가
    else:                                       # 연산 부호라면
        up = stack.pop()                        # 스택 맨위 추출 > up
        low = stack.pop()                       # 그다음 위 추출 > low
        result = eval(f"{low}{eq[idx]}{up}")    # low와 up을 연산부호를 활용하여 연산
        stack.append(result)                    # 연산 값은 다시 스택에 추가

print(f"{stack[0]:.2f}")