bracket_dict = {")":"(", "}":"{"}
T = int(input())
for t in range(1, T+1):
    txt = input()

    stack = []
    result = 1

    for c in txt:
        if c in ['(', "{"]:
            stack.append(c)
        elif c in [')', "}"]:
            if stack and bracket_dict[c] == stack.pop():
                pass
            else:
                result = 0
    else:
        if stack:
            result = 0

    print(f"#{t} {result}")