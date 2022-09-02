from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())    # 수의 개수
n_lst = list(map(int, input().split()))    # 입력받은 수열
sign = ["+","-","*","/"]
sign_lst = list(map(int, input().split()))
signs = []
for i in range(len(sign_lst)):
    signs.extend([sign[i]]*sign_lst[i])
pm_lst = set(list(permutations(signs, N-1)))  # set()으로 중복 순열은 제거

mx = -1e9; mn = 1e9
for op in pm_lst:
    n = n_lst[0]
    for i in range(1, N):
        if op[i-1] == "+":
            n += n_lst[i]
        elif op[i-1] == "-":
            n -= n_lst[i]
        elif op[i-1] == "*":
            n *= n_lst[i]
        else:
            if n < 0:
                n = -(-n//n_lst[i])
            else:
                n //= n_lst[i]
    if n > mx:
        mx = n
    if n < mn:
        mn = n

print(mx)
print(mn)


'''
2
5 6
0 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''