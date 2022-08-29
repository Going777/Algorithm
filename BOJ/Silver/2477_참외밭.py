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

# 제일 긴 가로 변 양옆 세로변 차이 > 뺄 삼각형 세로 길이
mx_w_idx = arr.index(mx_w)
sub_w = abs(arr[(mx_w_idx-1)%6] - arr[(mx_w_idx+1)%6])
# 제일 긴 세로 변 양옆 가로변 차이 > 뺄 삼각형 가로 길이
mx_h_idx = arr.index(mx_h)
sub_h = abs(arr[(mx_h_idx-1)%6] - arr[(mx_h_idx+1)%6])

# 최대 넓이에서 작은 사각형 넓이 빼기
s = (mx_w * mx_h) - (sub_w * sub_h)

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