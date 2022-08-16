import sys
sys.stdin = open('input.txt', 'r')

# 자기 방으로 돌아가기
# 겹치는 개수 찾기!! (빈도수)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    counts = [0]*200

    # 현재방부터 돌아갈 방까지 지나간 길 표시
    for _ in range(N): # N명의 학생
        s, e = map(int, input().split())
        if e < s:
            s, e = e, s
        counts[(s-1)//2:(e-1)//2+1] = list(map(lambda x: x+1, counts[(s-1)//2:(e-1)//2+1]))

    # 겹치는 최대 숫자 출력
    cnt = 0
    for num in counts:
        if cnt < num:
            cnt = num

    print(f"#{t} {cnt}")