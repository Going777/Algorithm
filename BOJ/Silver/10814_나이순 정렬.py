# age로 1차 정렬하고, age가 같다면 먼저 입력 받은 순서대로 정렬한다

N = int(input())
info = []
for i in range(N):
    age, name = input().split()
    info.append([i, int(age), name])

sorted_info = sorted(info, key=lambda x: (x[1], x[0]))
[print(data[1], data[2]) for data in sorted_info]
