'''
입력받은 영단어의 철자로 만들 수 있는 모든 단어 출력
중복 단어는 한 번만 출력
출력 시 알파벳 순서로 출력
'''
import sys
def solve(n, word):
    if n == N:
        # 여기서 중복을 체크해주게 되면 시간초과!!!
        print(word)
        return

    for i in range(N):
        if not visited[i]:
            tmp = word+str[i]
            # 여기서 중복되는 단어들을 걸러주어야 됨!
            if tmp not in record:
                visited[i] = 1
                record.add(tmp)
                solve(n+1, word+str[i])
                visited[i] = 0

T = int(sys.stdin.readline())
for _ in range(T):
    str = sorted(sys.stdin.readline().strip())  # 조건을 만족한 문자열을 바로 출력하기 위해 입력받은 문자열을 처음부터 정렬
    N = len(str)
    visited = [0]*N
    record = set()      # 중복 피하기 위해 탐색한 문자열 저장
    solve(0, '')

'''
2
abc
acba
'''