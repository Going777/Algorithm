'''
N개의 숫자가 공백없이 써있다
이 숫자를 모두 합해 출력하라
'''

import sys
input = sys.stdin.readline

N = int(input())
target = input().strip()
ans = 0

for n in target:
    ans += int(n)

print(ans)