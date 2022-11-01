'''
책을 박스에 넣어서 택배를 보내려 한다
책은 탑처럼 쌓여있기 때문에, 차례로 박스에 넣을 수밖에 없다
각각의 책은 무게가 있고, 박스는 최대로 넣을 수 있는 무게가 있을 때,
필요한 박스 개수의 최솟값은?
'''

N, M = map(int, input().split())    # N: 책의 개수 / M: 최대 무게
cnt = 0
if N == 0:                          # N == 0이면 cnt = 0
    print(cnt)
else:
    lst = list(map(int, input().split()))
    while lst:                      # lst가 비지 않을때까지 반복
        cnt += 1                    # 박스 수 +1
        tmp = 0                     # 무게
        while lst:
            if tmp + lst[0] > M:    # 박스에 담을 수 있는 최대 무게를 초과하면 종료
                break
            else:
                tmp += lst.pop(0)   # 무게 추가
    print(cnt)