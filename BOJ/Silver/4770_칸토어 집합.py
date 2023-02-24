# 칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 구간 [0, 1]에서 시작해
# 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.

# 1. -가 3N개 있는 문자열에서 시작한다.
# 2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다.
# 3. 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.

import sys

def divide(result):
    n = len(result)
    if n == 1:
        return result
    # 3등분 하고 각 구간별로 처리
    target = n // 3
    result[:target] = divide(result[:target])
    result[target:target*2] = [' ']*target
    result[target*2:] = divide(result[target*2:])
    return result

while True:
    try:
        N = int(sys.stdin.readline())
        result = ['-'] * (3**N)
        divide(result)
        print(''.join(result))
    except:
        break