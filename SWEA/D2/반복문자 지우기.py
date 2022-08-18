# def solve():
#     i = 1
#     while True:
#         if i-1 < 0 or i >= len(txt):
#             break
#         if txt[i-1] == txt[i]:
#             txt.pop(i)
#             txt.pop(i-1)
#             solve()
#         else:
#             i += 1
#
# T = int(input())
# for t in range(1, T+1):
#     txt = list(input())
#     solve()
#
#     print(f'#{t} {len(txt)}')
# ---------------------------------------------------------------------------------------
T = int(input())
for t in range(1, T+1):
    txt = input()
    stack = []

    for c in txt:
        if not stack:
            stack.append(c)
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
    print(f"#{t} {len(stack)}")
