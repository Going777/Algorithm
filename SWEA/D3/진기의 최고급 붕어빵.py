# N명 사람에게 판매
# 0초부터 붕어빵을 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다
def des_sort(lst):  # 내림차순 정렬 함수
    L = len(lst)
    for i in range(L-1):
        mx_idx = i
        for j in range(i+1, L):
            if lst[mx_idx] < lst[j]:
                mx_idx = j
        lst[mx_idx], lst[i] = lst[i], lst[mx_idx]
    return lst

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrived = des_sort(list(map(int, input().split())))
    ans = "Possible"
    time = [0]*(arrived[0]+1)

    tmp = M
    p = arrived.pop()
    for idx in range(len(time)):
        if idx == tmp:
            time[idx] = time[idx-1] + K
            tmp += M
        else:
            time[idx] = time[idx-1]

        if idx == p:
            time[idx] -= 1
            if time[idx] < 0:
                ans = "Impossible"
                break
            if arrived:
                p = arrived.pop()
            else:
                break

    print(f'#{tc} {ans}')

'''
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2
'''