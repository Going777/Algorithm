T = int(input())
class_list = list(map(int, input().split()))
B, C = map(int, input().split())

result = T # 총감독관은 클래스마다 한 명씩 존재
for cl in class_list:
    cl -=  B # 총감독관이 감독할 수 있는 학생 제외 응시생
    if cl > 0:
        result += (cl // C) # 부감독관 필요 숫자
        if cl % C: # 나누어 떨어지지 않고 남으면
            result += 1 # 부감독관 한 명 추가
        
print(result)
