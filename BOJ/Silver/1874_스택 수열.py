from sys import stdin

stack = []
result = []
num = 1

def solve(target):
    global num, result

    while num <= target:
        stack.append(num)
        result.append("+")
        num += 1

    if target == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        result = []
        return False

    return True

for _ in range(int(stdin.readline())):
    target = int(stdin.readline())
    if not solve(target):
        break

(print("\n".join(result)) if len(result) != 0 else print("NO"))