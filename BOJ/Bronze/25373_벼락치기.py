N = int(input())
condition = sum(range(1, 8)) # 7일 모두 시청해야 하는 경우의 최소 영상 개수 (기준점)
avg, rest = divmod(N, 7)
result = 0

# 모두 시청하는데 7일이 필요하지 않는 경우
if N < condition:
    num = 0
    num_sum = 0
    while num_sum < condition: 
        num += 1
        num_sum += num
    result = num

# 7일 모두 시청해야 하는 경우
else:
    if rest: # 7로 나눴을 때 나머지가 있으면, 나눠떨어질 때보다 하루를 더해줘야 함
        result += 1
    result += (avg + 3) # 7일 평균 값이 4일이므로, 3을 추가적으로 더해줘야 함

print(result)
