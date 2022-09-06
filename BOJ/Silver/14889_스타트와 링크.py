from itertools import combinations

# 각 인덱스에 맞는 값으로 능력치 합 구하기
def calc_abilities(idx_lst):
    abilities = 0
    for i in idx_lst:
        for j in idx_lst:
            abilities += S[i][j]
    return abilities

N = int(input())    # 총 인원 수(짝수)
S = [list(map(int, input().split())) for _ in range(N)]
target_N = N // 2    # 팀 당 인원
N_lst = set(range(N))

mn = 100*20
teams = []  # 모든 조합 저장
for team in combinations(N_lst, target_N):
    teams.append(team)

# 각 팀은 중간지점을 기준으로 symmetric하게 분포되어 있음 -> 절반까지만 검사하면 됨
for i in range(len(teams)//2):
    tmp = abs(calc_abilities(teams[i]) - calc_abilities(teams[-i-1]))
    # 최소값 구하기
    if tmp < mn:
        mn = tmp

print(mn)



'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''