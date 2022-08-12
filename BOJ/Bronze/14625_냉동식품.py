SH, SM = map(int, input().split())
EH, EM = map(int, input().split())
target = int(input())

count = 0
while True:
    
    # H와 M이 2자리수로만 받을 수 있기 때문에 10의자리수와 1의자리수만 비교하면 됨
    SH_a, SH_b = divmod(SH, 10)
    SM_a, SM_b = divmod(SM, 10)
    if (SH_a == target) or (SH_b == target) or (SM_a == target) or (SM_b == target):
        count += 1 
    
    # 시작시간 == 종료시간이면 카운트값 출력하고 반복문 종료
    if SH == EH and SM == EM: 
        print(count)
        break
    
    SM += 1 # 분 +=1
    # 60분이 되면 시간을 +1 해주고 분은 다시 초기화
    if SM == 60:
        SH += 1
        SM = 0
