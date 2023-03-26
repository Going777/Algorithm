# 저울과 몇 개의 추가 주어졌을 때, 이를 이용해 주어진 구슬의 무게를 확인할 수 있는지 알아보고자 함

import sys
input = sys.stdin.readline
n = int(input())    # 추의 개수 (30이하)
weights = list(map(int, input().split()))   # 추의 무게가 가벼운것 부터 주어짐 / 같은 무게 여러개 있을 수도(500g이하)
m = int(input())  # 구슬 개수(7이하)
targets = list(map(int, input().split()))   # 확인하고자 하는 구슬 무게(40000이하 자연수)

possible = set()    # 가능한 무게를 저장하는 리스트(집합)
# 가능한 무게 리스트 구성 조건
    # 1. 본인 무게
    # 2. 새로운 무게가 들어왔을 때, (본인 - 새로운 무게)의 절댓값
    # 3. 새로운 무게가 들어왔을 때, (본인 + 새로운 무게)
for w in weights:
    next = {w}                  # 새로운 무게 그 자체로 가능한 무게 리스트로 포함 가능
    for temp in possible:
        next.add(abs(temp-w))   # 가능한 무게 집합에서 새로운 무게를 뺀 것 만큼 가능성 무게 리스트에 추가
        next.add(temp+w)        # 가능한 무게 집합에서 새로운 무게를 더한 것 만큼 가능성 무게 리스트에 추가
    possible |= next            # 기존의 가능한 무게 리스트와 새로운 가능성 무게 리스트 합치기

for t in targets:
    if t in possible:
        print("Y", end=" ")
    else:
        print("N", end=" ")