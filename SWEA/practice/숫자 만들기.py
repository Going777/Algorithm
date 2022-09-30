'''
N개의 숫자가 적혀있는 게임 판이 있고, + - * / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과를 보고자 한다
수식 계산 시, 연산자의 우선순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다
결과가 최대가 되는 수시과 최소가 되는 수식을 찾고, 두 값의 차이를 구하라
    3 <= N <= 12
    연산자 카드 개수의 총합은 항상 N-1
    게임판의 숫자는 1이상 9이하의 정수
    숫자와 숫자 사이에는 하나의 연산자만
    나눗셈 계산 시 소수점 이하는 버림
    입력으로 주어지는 숫자의 순서 변경 불가
    연산 중 값은 -100,000,000 이상 100,000,000 이하임이 보장됨
'''
def calc(a, b, op):
    if op == 0:
        return a+b
    elif op == 1:
        return a-b
    elif op == 2:
        return a*b
    else:
        return int(a/b)

def dfs(n, result):
    global mx, mn
    if n == N-1:
        if result > mx:
            mx = result
        if result < mn:
            mn = result
    for i in range(4):
        if op_nums[i]:
            op_nums[i] -= 1
            dfs(n+1, calc(result, nums[n+1], i))
            op_nums[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_nums = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mx = -100000000
    mn = 100000000
    dfs(0, nums[0])

    print(f'#{tc} {mx-mn}')



'''
1
5
2 1 0 1
3 5 3 7 9
'''