import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

def solve(n, cards):
    lis = [] # LIS(최장 증가 부분 수열)
    for card in cards:
        pos = bisect_left(lis, card) # LIS 위치 찾기
        if pos == len(lis):
            lis.append(card)
        else:
            lis[pos] = card # LIS 값 갱신
    return n - len(lis) # 최소 제거 카드 수 계산

print(solve(N, cards))