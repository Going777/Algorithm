def selectionSort(arr, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

N = 9
arr = [int(input()) for _ in range(N)]
s_target = 100
s_arr = sum(arr)
is_find = False

for i in range(N-1):
    for j in range(i+1, N):
        if s_arr - arr[i] - arr[j] == s_target:
            spyA = arr[i]
            spyB = arr[j]
            is_find = True
            break
    if is_find:
        arr.remove(spyA)
        arr.remove(spyB)
        break

M = len(arr)
sorted_arr = selectionSort(arr, M)

[print(x) for x in sorted_arr]