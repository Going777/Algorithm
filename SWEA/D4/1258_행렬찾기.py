def my_sort(lst):
    M = len(lst)
    tmp = []
    for i in range(M-1):
        mn_idx = i
        for j in range(i+1, M):
            eq1 = lst[mn_idx][0]*lst[mn_idx][1]
            eq2 = lst[j][0]*lst[j][1]
            if eq1 > eq2:
                mn_idx = j
            elif eq1 == eq2:
                if lst[mn_idx] > lst[j]:
                    mn_idx = j
        lst[i], lst[mn_idx] = lst[mn_idx], lst[i]
        tmp.extend(lst[i])
    tmp.extend(lst[-1])
    return tmp

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    counts = [0]*(N+1)
    result = []

    for i in range(N):
        tmp = 0
        for j in range(N+1):
            if arr[i][j] == 0:
                counts[tmp] += 1
                tmp = 0
            else:
                tmp += 1

    cnt = 0
    for idx in range(1, N):
        if counts[idx] != 0:
            cnt += 1
            result.append([counts[idx], idx])

    result = my_sort(result)
    print(f"#{tc} {cnt}", *result)

'''
3
5
1 2 3 4 0 
0 0 0 0 0 
5 0 0 0 0 
6 0 0 0 0 
0 0 0 0 0 
8
1 2 3 0 0 4 5 0 
6 7 8 0 0 0 0 0 
9 1 2 0 0 3 0 0 
4 5 6 0 0 7 0 0 
0 0 0 0 0 8 0 0 
9 1 2 3 0 4 0 0 
5 6 7 8 0 9 0 0 
0 0 0 0 0 0 0 0 
20
1 2 3 4 5 6 7 8 0 0 9 1 0 0 0 0 0 0 0 0 
2 3 4 5 6 7 8 9 0 0 0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 8 0 0 9 1 2 3 4 5 6 0 0 0 
7 8 9 1 2 3 4 5 0 0 6 7 8 9 1 2 3 0 0 0 
4 5 6 7 8 9 1 2 0 0 3 4 5 6 7 8 9 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
2 0 0 0 0 0 0 0 0 0 3 4 5 6 7 0 0 0 0 0 
8 0 0 0 0 0 0 0 0 0 9 1 2 3 4 0 0 0 0 0 
5 0 0 0 0 0 0 0 0 0 6 7 8 9 1 0 0 0 0 0 
2 0 0 0 0 0 0 0 0 0 3 4 5 6 7 0 0 0 0 0 
8 0 0 0 0 0 0 0 0 0 9 1 2 3 4 0 0 0 0 0 
5 0 0 0 0 0 0 0 0 0 6 7 8 9 1 0 0 0 0 0 
2 0 0 0 0 0 0 0 0 0 3 4 5 6 7 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 8 9 1 2 3 0 0 0 0 0 
4 5 6 0 0 0 0 0 0 0 7 8 9 1 2 0 0 0 0 0 
3 4 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
'''