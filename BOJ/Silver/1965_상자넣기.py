# 앞에 있는 상자의 크기가 뒤에 있는 상자 크기보다 작으면 상자를 뒤 상자에 넣을 수 있다
# 상자의 크기가 리스트로 주어질 때, 한 번에 넣을 수 있는 최대의 상자 개수를 출력하라
# 상자의 크기는 1000을 넘지 않는 자연수

import sys
input = sys.stdin.readline

N = int(input())    # 상자의 개수
lst = list(map(int, input().split()))
print(lst)
cnt = 0
target = lst[0]
for i in range(1, N):
    if lst[i] > target:
        cnt += 1
    target = lst[i]
print(cnt)