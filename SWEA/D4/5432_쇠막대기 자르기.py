T = int(input())
for t in range(1, T+1):
    txt = list(input())
    lst = []
    stick_cnt = 0
    result = 0
    for i in txt:
        if i == "(":
            lst.append(i)
            stick_cnt += 1
        else:
            if lst[-1] == "(":    # 레이저 부분
                stick_cnt -= 1
                result += stick_cnt
                lst.append(i)
            else:                   # 쇠막대기가 끝나는 부분
                result += 1
                stick_cnt -= 1

    print(f"#{t} {result}")-]