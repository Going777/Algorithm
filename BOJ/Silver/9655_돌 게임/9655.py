import sys
input = sys.stdin.readline

# 턴을 돌아가며 돌 1개 또는 3개를 가져갈 수 있다
# 마지막으로 돌을 가져가는 사람이 이긴다
# 상근이가 먼저 시작

N = int(input())

print("SK" if N % 2 else "CY")
