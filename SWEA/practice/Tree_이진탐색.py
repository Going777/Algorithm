def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)
        lst[n] = cnt
        cnt += 1
        inorder(n*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    cnt = 1
    inorder(1)

    print(f"#{tc} {lst[1]} {lst[N//2]}")

'''
3
6
8
15
'''