import sys
input = sys.stdin.readline

N = int(input())
lst = list(input().strip() for _ in range(N))
result = ""
idx1 = lst.index("KBS1")
idx2 = lst.index("KBS2")

result += "1" * idx1
result += "4" * idx1
if idx1 > idx2: idx2 += 1
result += "1" * idx2
result += "4" * (idx2 - 1)
print(result)