T = int(input())
class_list = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for cl in class_list:
    result += 1 # 총감독관은 무조건 한 명
    remain = cl - B # 총감독관이 감독할 수 있는 학생 제외 응시생
    result += remain // C # 부감독관 필요 숫자
    if remain % C != 0: # 나누어 떨어지지 않고 남으면
        result += 1 # 부감독관 한 명 추가
        
print(result)
