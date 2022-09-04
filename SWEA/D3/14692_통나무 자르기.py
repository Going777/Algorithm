T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 통나무 길이
    if N % 2:
        print(f"#{tc} Bob")
    else:
        print(f"#{tc} Alice")

'''
5
2
3
10
50
100
'''