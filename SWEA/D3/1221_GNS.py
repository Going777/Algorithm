T = int(input())
for _ in range(T):
    t, N = input().split()
    arr = list(input().split())
    condition = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0] * len(condition)
    for i in range(len(condition)):
        for j in range(len(arr)):
            if condition[i] == arr[j]:
                counts[i] += 1
 
    print(t)
    for i in range(len(condition)):
        if counts[i]:
            print((condition[i]+" ")*counts[i], end="")
    print(end="\n")
