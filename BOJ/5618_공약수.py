from functools import reduce

# 유클리드 호제법으로 최대 공약수 구하기
def GCD(A, B):
    if B > A:
        A, B = B, A
    while B != 0:
        A, B = B, A%B
    return A

N = int(input())
num_list = list(map(int, input().rstrip().split()))
# num_list내에서 요소 2개씩 차례로 GCD 함수 적용하여 최종 최대 공약수 구하기
gcd = reduce(GCD, num_list)

# 최대 공약수의 약수 구하기
result = set()
for num in range(1, int(gcd**0.5) + 1): 
    if gcd % num == 0:
        result.update([num, gcd//num])                    
result = sorted(list(result))

# 요소 하나씩 출력
for num in result:
    print(num)
