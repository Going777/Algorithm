'''
사람의 번호는 1~N번까지 존재
i번 사람에게 인사하면 L[i]만큼 체력을 잃고, J[i]만큼 기쁨을 얻는다
목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것
기본값 : 체력 100, 기쁨 0
만약 체력이 0보다 작아지면, 죽어서 아무런 기쁨을 못느낀 것
'''
def dfs(n, power, joy):
    global mx
    if power <= 0:                  # 체력이 0이하이면 return
        return

    if mx < joy:                    # 최대 기쁨값 갱신
        mx = joy

    if n == N:                      # 모두 순회했다면 종료
        return

    dfs(n+1, power-L[n], joy+J[n])  # 인사한 경우
    dfs(n+1, power, joy)            # 인사안한 경우


N = int(input())                        # 사람 수
L = list(map(int, input().split()))     # 체력 -
J = list(map(int, input().split()))     # 기쁨 +
mx = 0
dfs(0, 100, 0)
print(mx)