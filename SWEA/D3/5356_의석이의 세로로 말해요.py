import sys
sys.stdin = open('../D2/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    result = ""
    txt_arr = [list(input()) for _ in range(5)]
    # 5개씩 입력받은 리스트 중에서 가장 긴 길이 찾기
    lens = [len(row) for row in txt_arr]
    max_len = 0
    for l in lens:
        if max_len < l:
            max_len = l

    for j in range(max_len):
        for i in range(5):
            try:
                result += txt_arr[i][j]
            except:
                result += ""

    print(f"#{t} {result}")