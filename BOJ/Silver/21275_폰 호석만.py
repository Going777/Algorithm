'''
수 3개 X(10진법),A,B를 결정한다
X를 A진법으로 표현한 수와 B진법으로 표현한 수를 종이에 써 놓는다
종이에 써있는 두 수를 통해 원래 숫자인 X,A,B를 계산해라
조건을 만족하는 (X,A,B)로 가능한 조합이 여러개라면 'Multiple'을 출력하고,
가능한 조합이 없다면 'impossible'을 출력하라

각 자리수는 0이상 z이하 (a: 10 ~ z: 35)
'''
import sys
import string

def calc(target):
    lst_target = list(map(dic.get, list(target)))   # 입력받은 문자를 모두 숫자로 바꿔서 리스트에 저장
    lst_target = list(map(int, lst_target))[::-1]   # 진법 계산을 위해 거꾸로 뒤집음
    mx = max(lst_target)                            # 가장 큰 값 찾기 (해당값+1 부터 35까지가 가능한 진법 범위)
    decimal = []
    for n in range(mx+1, 36):
        tmp = 0                                     # n진법 -> 10진법 바꾸기
        for idx in range(len(lst_target)):
            tmp += lst_target[idx] * (n**idx)
            if tmp >= 2**63:                        # 해당값이 2**63이상이라면 범위 초과 > 중단
                break
        else:
            decimal.append([n, tmp])                # [진법, 10진법수] 형태로 추가해서 저장
    return decimal

def solve(lst1, lst2):
    ans = []
    for n_A in lst1:
        for n_B in lst2:
            if n_A[1] == n_B[1] and n_A[0] != n_B[0]:   # 같은 10진법수를 찾았고, 진법이 다르다면
                if ans:                                 # ans에 이미 값이 있으면 Multiple
                    return 'Multiple'
                else:                                   # 값이 없으면 문제 요구 포맷대로 추가
                    ans.append([n_A[1], n_A[0], n_B[0]])
    if not ans:                             # 일치하는 진법 및 수가 없다면
        return 'Impossible'                 # Impossible 출력
    return ' '.join(list(map(str, ans[0]))) # 지금까지 탈출 못했다면 해당하는 하나의 진법 및 수를 찾은 것 > 포맷에 맞게 출력

dic = dict(zip(map(str, range(10)), range(10)))     # 0~z까지에 해당하는 숫자를 딕셔너리 형태로 만들기
dic.update(dict(zip(string.ascii_lowercase, range(10, 36))))
n_A, n_B = sys.stdin.readline().strip().split()     # X를 A,B진법으로 표현한 값

if (n_A == '0') or (n_B == '0'):    # 입력받은 수 중 하나라도 0이 있으면
    print('Multiple')               # 2~35진법 모두 가능 > Multiple
else:
    n_A_lst = calc(n_A)
    n_B_lst = calc(n_B)
    print(solve(n_A_lst, n_B_lst))
