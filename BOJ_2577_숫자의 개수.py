A = int(input())
B = int(input())
C = int(input())

target = A * B * C 
target_list = list(map(int, str(target)))

for num in range(10):
    print(target_list.count(num))
