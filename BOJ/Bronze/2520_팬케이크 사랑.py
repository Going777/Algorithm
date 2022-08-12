T = int(input())

for _ in range(T):
    input()
    dough_input = list(map(int, input().split()))
    toping_input = list(map(int, input().split()))

    dough_16 = [8, 8, 4, 1, 9] # 16개 반죽 만들 수 있는 양
    toping = [1, 30, 25, 10] # 종류별 필요한 토핑 양

    toping_num = sum([toping_input[idx] // toping[idx] for idx in range(len(toping))])
    dough_num = min([dough_input[idx] * 16 // dough_16[idx] for idx in range(len(dough_16))])

    print(min(toping_num, dough_num))
