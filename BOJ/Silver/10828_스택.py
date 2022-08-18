import sys

N = int(sys.stdin.readline())                    # 명령의 수
stack = []
for _ in range(N):                  # 명령의 개수만큼 반복
    txt = sys.stdin.readline().split()
    cmd = txt[0]
    if len(txt) == 2:
        x = txt[1]

    if cmd == 'push':
        stack.append(x)
    elif cmd == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)