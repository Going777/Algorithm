import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = 0

    i = N//2                            # 중간지점부터 하나씩 내려오면서 탐색
    for _ in range(N):
        if i == 0:                      # 제일 앞에까지 찾게 되었다면, i를 N으로 할당
            i = N
        row = list(map(int, input()))   # N번만큼 row를 받아옴
        if i <= N-i:                    # 현재 i번째 인덱스에서 N-i-1번째까지의 합을 result에 더해줌
            result += sum(row[i:N-i])
        else:                           # i가 N으로 바뀌어 뒤에서부터 와야할때는 인덱스를 반대로
            result += sum(row[N-i:i])
        i -= 1

    print(f"#{t} {result}")




def my_sort(arr):   # 오름차순 정렬 함수
    lst = arr[:]                                    # 얕은 복사
    for i in range(N):
        m_idx = i                                   # 현재 기준 위치
        for j in range(i+1, N):
            if lst[m_idx] > lst[j]:                 # 현재 기준 위치 값보다 j번째 값이 더 작다면
                m_idx = j                           # 기준 위치를 변경
        lst[i], lst[m_idx] = lst[m_idx], lst[i]     # 배열에서 해당 인덱스 값들 스왑
    return lst

N = int(input())
target = []                                         # 만들고자 하는 수열
for _ in range(N):
    target.append(int(input()))

stack = []
result = []
lst = my_sort(target)                               # 스택에는 오름차순으로 넣어야하므로 정렬필요
isNotPossible = False                               # 해당 수열을 만들 수 있는지 없는지
for t in target:
    while True:
        if lst and lst[0] <= t:                   # lst가 비지 않았고, 인덱스 번째의 값이 타겟값보다 작거나 같다면
            stack.append(lst[0])                  # 스택에 해당 값 추가
            result.append("+")                      # result += "+"
            if lst[0] == t:                       # 같은 경우
                stack.pop()                         # 스택에서 제거
                result.append("-")                  # result += "-"
                lst.pop(0)                        # 리스트에서도 제거
                break                               # 해당 타겟값은 처리 완료 했으므로 다음 타겟값으로 가기 위해 break
            lst.pop(0)                            # 타겟값을 찾지 못했다면 현재 값을 리스트에서 제거
            continue                                #
        else:
            if t == stack[-1]:
                stack.pop()
                result.append("-")
            else:
                result = []
                isNotPossible = True
                break
    if isNotPossible:
        break

if result:
    [print(x) for x in result]
else:
    print("NO")
