import sys
sys.stdin = open('../D2/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    txt = input()
    stack = []
    result = 1 # 괄호 짝 맞는지 여부(맞으면 1 아니면 0)

    for c in txt:
        if c == "(": # 여는 괄호는 스택에 추가
            stack.append(c)
        else: # 닫는 괄호인 경우
            if len(stack) == 0: # 스택이 비었다면 짝을 맞출 수가 없음 > 종료
                result = 0
                break
            # elif stack[-1] == "(": # 스택의 마지막 원소가 "("라면 짝이 맞음으로 스택의 마지막 원소 제거
            else: # 스택에는 '('만 들어가 있으므로, 위의 조건 확인 작업 필요 없음
                stack.pop()
    if stack: # 모든 원소 다 검사후, 스택에 여전히 원소가 남아있다면 짝이 맞지 않는 것
        result = 0

    print(f"#{t} {result}")