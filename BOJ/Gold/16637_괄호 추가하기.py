import sys

N = int(sys.stdin.readline()) # 수식의 길이
eq = input() # 수식

def calc(num1, sign, num2):
    # 연산자는 +, -, * 중 하나
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    else:
        return num1 * num2

def dfs(idx, value):
    if idx == N-1:
        return
