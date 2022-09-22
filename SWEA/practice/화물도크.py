T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append([s, e])
    arr = sorted(arr, key=lambda x: x[1])

    ans = 1
    prev_e = arr[0][1]
    for work in arr:
        s, e = work
        if prev_e <= s:
            ans += 1
            prev_e = e

    print(f'#{tc} {ans}')

'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''