# T = int(input())
# for tc in range(1, T+1):
#     txt = input()
#     stack = []
#     prior = {"*": 2, "+": 1}        # 우선순위 * > +
#     result = ""
#     for t in txt:
#         if t.isnumeric():                                   # 연산자가 아닌 숫자라면
#             result += t                                     # 최종 결과값에 추가
#         else:                                               # 연산자라면
#             while stack and prior[t] <= prior[stack[-1]]:   # 스택이 비거나 현재 연산자의 우선순위보다 스택 마지막 원소의 우선순위가 더 높아질 때까지
#                 result += stack.pop()                       # 스택에서 연산자를 추출하고 최종 결과값에 추가
#             stack.append(t)                                 # 해당 조건을 다 만족시켰다면, 스택에 현재 연산자 추가
#
#     while stack:                                            # 남아 있는 연산자 최종 결과값에 뒤에서부터 차례대로 추가
#         result += stack.pop()
#
#     print(f"#{tc} {result}")

def f(i, N):
    if i == N:
        print(P)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, 3)