import sys

T = int(sys.stdin.readline())
for _ in range(T):
    str = sys.stdin.readline().strip()
    stack = []
    result = "YES"
    for c in str:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                result = "NO"
                break
    else:
        if stack:
            result = "NO"
    print(result)