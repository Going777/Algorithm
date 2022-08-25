import sys
sys.stdin = open('input.txt', 'r')

def my_sort(lst):
    for i in range(N-1):
        mn_idx = i
        for j in range(i+1, N):
            if lst[mn_idx] > lst[j]:
                mn_idx = j
        lst[mn_idx], lst[i]  = lst[i], lst[mn_idx]
    return lst

def solve():
    if M > customer[0]:             # 처음 붕어빵을 만들기도 전에 첫 번째 손님이 입장하면 불가능
        return "Impossible"

    tmp = 0
    for i in range(M, len(cnt)):
        if i % M == 0:              # M번째 시간에 해당될때마다 붕어빵은 K개 만큼 늘어남
            tmp += K
        for t in customer:
            if i == t:              # 손님이 등장한 시간이면
                tmp -= 1            # 지금껏 만든 붕어빵에서 -1
                break
        if tmp < 0:                 # 손님에게 붕어빵을 주고난 후 음수가 된다면
            return "Impossible"     # 해당 손님에게 붕어빵을 줄 수 없던 것 > 불가능
            break
        cnt[i] = tmp                # 위 조건에서 걸러지지 않으면 지금까지 남은 붕어빵 개수 현재 시간에 추가
    return "Possible"


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N: 예약 수 / M: 붕어빵 만드는 데 드는 시간 / K: M시간 일했을 때 산출되는 붕어빵 개수
    customer = my_sort(list(map(int, input().split())))     # 손님들이 입장하는 시간 (오름차순 정렬)
    cnt = [0]*(customer[-1]+1)                              # 시간에 따른 붕어빵 개수 기록 (마지막으로 입장하는 손님에 해당하는 시간까지 만들어주어야 함)

    ans = solve()

    print(f"#{tc} {ans}")

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