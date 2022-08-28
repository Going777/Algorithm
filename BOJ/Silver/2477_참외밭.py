K = int(input())    # 1m^2에서 자라는 참외 개수
mx_w = mx_h = 0
arr = []
for _ in range(6):
    # 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
    direct, distance = map(int, input().split())
    if direct in [3, 4]:
        mx_w = distance if distance > mx_w else mx_w
    else:
        mx_h = distance if distance > mx_h else mx_h
    arr.append(distance)

N = len(arr)
mx_w_idx = arr.index(mx_w)
mx_h_idx = arr.index(mx_h)
if mx_w_idx < mx_h_idx:
    if mx_w_idx == 0 and mx_h_idx == N-1:
        idx1 = 2
        idx2 = 3
    else:
        idx1 = (mx_h_idx + 2) % 6
        idx2 = (idx1 + 1) % 6
else:
    if mx_h_idx == 0 and mx_w_idx == N-1:
        idx1 = 2
        idx2 = 3
    else:
        idx1 = (mx_w_idx + 2) % 6
        idx2 = (idx1 + 1) % 6

s = (mx_w * mx_h) - (arr[idx1] * arr[idx2])

print(s*K)

'''
7
4 50
2 160
3 30
1 60
3 20
1 100

7
4 50
1 60
3 20
1 100
3 30
2 160

7
4 50
2 160
3 30
1 60 
3 20
1 100
'''