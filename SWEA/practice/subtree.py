def subtree(N):
    global cnt
    if N:
        cnt += 1
        subtree(ch1[N])
        subtree(ch2[N])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(0, E*2, 2):
        p = lst[i]
        c = lst[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    subtree(N)
    print(f"#{tc} {cnt}")

'''
3
19 1
20 1 20 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''