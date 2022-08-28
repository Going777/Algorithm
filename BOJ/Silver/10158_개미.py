import sys
input = sys.stdin.readline

def solve(x, s, lst):               # x: 현재 위치(가로/세로) / s: (가로/세로) / lst: (가로/세로 방향 리스트)
    q = (x+t) // s
    r = (x+t) % s

    if q % 2 == 0:
        if r == 0:
            result.append(lst[0])
        else:
            result.append(lst[r])
    elif q % 2 == 1:
        if r == 0:
            result.append(lst[-1])
        else:
            result.append(lst[-r-1])

w, h = map(int, input().split())    # 가로 / 세로
p, q = map(int, input().split())    # 초기 위치
t = int(input())                    # t시간 후 위치는?

w_lst = list(range(w+1))
h_lst = list(range(h+1))

result = []
solve(p, w, w_lst)
solve(q, h, h_lst)

print(*result)

# dx = [1,-1,-1,-1]
# dy = [1,1,-1,1]
#
# x, y = p, q
# k = 0
# cnt = 0
# while True:
#     if cnt == t:
#         break
#     nx = x + dx[k]; ny = y + dy[k]
#     if 0 <= nx <= w and 0 <= ny <= h:
#         x = nx; y = ny
#         cnt += 1
#     else:
#         k = (k+1) % 4
#
# print(*[x, y])

'''
6 4
4 1
8

5 5
3 3
2
'''