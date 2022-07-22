t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    divisor = 0 # 최대 공약수
    min_num = min(A, B)
    
    for num in range(min_num, 0, -1):
        if (A % num == 0) and (B % num == 0):
            divisor = num
            break
    
    multiple = divisor * (A // divisor) * (B // divisor) # 최소 공배수
    print(multiple)

---------------------------------------------------------------------

# 유클리드 호제법을 사용한 풀이
def GCD(A, B):
    if B > A:
        A, B  = B, A
    while B != 0:
        A, B = B, A % B
    return A

for _ in range(int(input())):
    A, B = map(int, input().split())
    gcd = GCD(A, B)
    print((A * B) // gcd)
