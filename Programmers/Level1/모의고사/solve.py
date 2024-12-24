def solution(answers):
    N = len(answers)
    p1 = [1,2,3,4,5] * 2000
    p2 = [2,1,2,3,2,4,2,5] * 1250
    p3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt_lst = [0, 0, 0]

    for i in range(N):
        if p1[i] == answers[i]:
            cnt_lst[0] += 1
        if p2[i] == answers[i]:
            cnt_lst[1] += 1
        if p3[i] == answers[i]:
            cnt_lst[2] += 1


    p_lst = []
    mx_cnt = max(cnt_lst)
    for idx, val in enumerate(cnt_lst):
        if val == mx_cnt:
            p_lst.append(idx + 1)

    return p_lst

solution([1,2,3,4,5])
solution([1,3,2,4,2])