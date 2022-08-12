S = int(input())
n = 0
m_sum = 0
while m_sum < S:
    n += 1
    m_sum += n
if S < m_sum:
    n -= 1
print(n)
