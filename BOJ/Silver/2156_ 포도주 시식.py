'''
포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원위치
연속으로 놓여있는 3잔을 모두 마실수는 없다
될 수 있는 대로 많은 양의 포도주를 맛보기 위해 어떤 포도주 잔을 선택해야 할까
1~n까지의 포도주잔이 순서대로 놓여있다
'''

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
table = [0]*n

if n == 1:
    table[0] = lst[0]
elif n == 2:
    table[1] = sum(lst)
else:
    table[0] = lst[0]
    table[1] = sum(lst[:2])
    table[2] = max(lst[0]+lst[2], table[1], lst[1]+lst[2])
    for idx in range(3, n):
        table[idx] = max(table[idx-2]+lst[idx], table[idx-1], table[idx-3]+lst[idx-1]+lst[idx])

print(table[n-1])

'''
6
6
10
13
9
8
1
'''