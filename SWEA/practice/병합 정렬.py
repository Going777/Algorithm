def merge_sort(lst):
    global cnt
    # 종료 조건
    if len(lst) <= 1:
        return lst

    # 분할
    m = len(lst)//2         # 중간값 인덱스
    l = merge_sort(lst[:m]) # 왼쪽 그룹
    r = merge_sort(lst[m:]) # 오른쪽 그룹

    # 문제 요구사항
    if l[-1] > r[-1]:   # 왼쪽 그룹의 마지막 원소가 오른쪽 그룹의 마지막 원소보다 크다면
        cnt += 1        # cnt + 1

    # 병합
    merged_lst = []     # 병합 배열
    len_l = len(l)
    len_r = len(r)
    i = 0               # 왼쪽 배열 인덱스
    j = 0               # 오른쪽 배열 인덱스
    # 각 그룹 모두에 데이터가 남아있는 동안 반복
    while i < len_l and j < len_r:
        # 각 그룹의 맨 앞 데이터 값 비교(더 작은 값 병합 배열에 추가)
        if l[i] < r[j]:
            merged_lst.append(l[i])
            i += 1
        else:
            merged_lst.append(r[j])
            j += 1

    # 각 그룹에 데이터가 남아있는 경우 처리
    # 남은 원소가 없거나 l 또는 r 그룹 중 한 그룹에만 원소가 남아있을 것이므로 코드 순서 신경X
    while i < len_l:
        merged_lst.append(l[i])
        i += 1
    while j < len_r:
        merged_lst.append(r[j])
        j += 1

    return merged_lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    m_lst = merge_sort(lst)
    print(f'#{tc} {m_lst[N//2]} {cnt}')

'''
3
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
100
158 56 163 106 108 153 159 147 93 140 126 9 145 166 191 106 48 183 184 115 197 136 45 196 175 89 199 52 186 170 199 28 190 40 83 48 151 35 128 4 13 38 65 20 76 142 23 63 30 30 178 36 32 114 79 68 2 187 106 98 67 131 109 177 20 113 1 102 172 119 197 190 28 82 165 168 60 18 156 174 78 42 110 63 56 66 191 105 72 108 104 198 179 132 99 189 183 91 28 162 
'''