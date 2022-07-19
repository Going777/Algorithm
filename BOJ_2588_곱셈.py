# 세 자릿수 X 세 자릿수 곱셈 과정을 코드로 나타내 보는 문제

num1 = int(input())
num2 = int(input())
eq_answer = []

for idx, digit in enumerate(str(num2)[::-1]):
    answer = num1 * int(digit)
    eq_answer.append(answer * (10 ** idx))
    print(answer)
eq_answer.append(sum(eq_answer))

print(eq_answer[-1])
