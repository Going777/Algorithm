'''
학생들은 접속 순서대로 3번부터 N+2번까지 입장번호를 받게 된다
한 학생에서 출석 코드를 보내게 되면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게
출석 코드를 보내 해당 강의의 출석을 할 수 있게끔 한다
K명 의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생에게 보내지 않는다
무작위로 한 명에게 출석 코드를 보내는 행위를 Q번 반복한 뒤,
특정 구간의 입장 번호를 받은 학생들 중 출석이 되지 않은 학생 수를 구하고자 한다
'''

N, K, Q, M = map(int, input().split())
sleeps = list(map(int, input().split()))
starts = list(map(int, input().split()))
# stu_num = [1]*(N+3)
stu_num = list(range(N+3))
stu_num[0], stu_num[1], stu_num[2] = 0, 0, 0
for i in sleeps:
    stu_num[i] = -1

for s in starts:
    tmp = s
    while tmp < N+3:
        if tmp == -1:
            break
        elif tmp in sleeps:
            tmp += s
            continue
        stu_num[tmp] = 0
        tmp += s

for _ in range(M):
    S, E = map(int, input().split())
    print(sum(stu_num[S:E+1]))


'''
10 1 3 1
7
3 5 7
3 12

5 1 1 1
3
3
3 7
'''