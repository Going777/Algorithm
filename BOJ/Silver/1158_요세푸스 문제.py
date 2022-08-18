import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))           # 기준 배열
result = []                         # 정답 배열

idx = 0
while arr:
    idx += K-1                      # 인덱스 값이 K-1의 배수인곳 제거
    if idx >= len(arr):             # 인덱스 값이 배열 크기 보다 크거나 같아진다면,
        idx %= len(arr)             # 해당 인덱스 값은 그 값을 배열 크기로 나눈 나머지 값으로 설정
    result.append(arr.pop(idx))     # 정답 배열에 인덱스에 해당하는 값 넣어주고, 기준 배열에서는 삭제

print(f"<{', '.join(map(str,result))}>")

