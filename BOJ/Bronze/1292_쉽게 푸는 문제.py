start, end = map(int, input().split())
max_num = max(start, end)

target = "" # 문제에서 제시한 수열 만들기
num = 1
while True:
    if len(list(target.split())) > max_num:
        target_ls = list(map(int, target.split()))
        break
    target += (str(num)+" ") * num # 한자리 숫자일 경우 상관없지만, 두자리 이상이되면 숫자간 구분이 안되므로 공백 필요
    num += 1 

print(sum(target_ls[start-1:end]))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# list에서 append는 하나씩밖에 안되지만 extend는 곱하기 연산을 통해 같은 값을 여러개 추가할 수 있다! (+= 연산과 같은 기능)
lst =[]
for i in range(46):
    lst += [i] * i
    # lst.extend([i] * i)
A, B = map(int, input().split())

ans = 0
for i in range(A-1, B):
    ans += lst[i]

print(ans)
