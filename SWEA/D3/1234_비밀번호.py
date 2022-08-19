import sys
sys.stdin = open('input.txt', 'r')

T = 10
for t in range(1, T+1):
    N, txt = input().split()
    stack = []

    for i in range(int(N)):
        if not stack:
            stack.append(txt[i])
        else:
            if stack[-1] == txt[i]:
                stack.pop()
            else:
                stack.append(txt[i])

    print(f"#{t} {''.join(stack)}")