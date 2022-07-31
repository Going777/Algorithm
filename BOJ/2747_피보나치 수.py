# 피보나치 수열을 재귀함수로 구현해봄
# 시간초과
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))

------------------------------------------------------------------------------------------------------

# 입력 받는 N은 45보다 작거나 같다
# 따라서 45번째까지 확인 가능한 피보나치 수열 리스트를 미리 만든 후 인덱스로 접근하는 방식으로 시간초과 해결
fibo = [0] * 46
fibo[1] = 1

for i in range(46-2):
    fibo[i+2] = fibo[i] + fibo[i+1]

N = int(input())
print(fibo[N])
