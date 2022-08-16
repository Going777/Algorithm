import sys
sys.stdin = open('input.txt', 'r')

def findMax(arr):
    max_v = arr[0]
    for x in arr:
        if x > max_v:
            max_v = x
    return max_v

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = 0
    loss = 0

    while arr:
        maxV = findMax(arr)
        for i in range(len(arr)):
            if arr[i] == maxV:
                loss += sum(arr[:i])
                profit += i * arr[i]
                arr = arr[i+1:]
                break
        else:
            break

    print(f"#{t} {profit - loss}")