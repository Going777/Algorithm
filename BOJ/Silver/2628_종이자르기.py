def findMaxLeng(arr):
    mx = 0
    prev = 0
    for t in arr:
        tmp = t-prev
        if mx < tmp:
            mx = tmp
        prev = t
    return mx

w, h = map(int, input().split())
N = int(input())
cuts = [[], []]
for _ in range(N):
    cond, cut = map(int, input().split())
    cuts[cond].append(cut)

cuts[0].sort()
cuts[1].sort()
cuts[0].append(h)
cuts[1].append(w)

mx_h = findMaxLeng(cuts[0])
mx_w = findMaxLeng(cuts[1])

print(mx_w*mx_h)