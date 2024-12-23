from collections import deque

def solution(begin, target, words):
    answer = 0
    # target이 words에 없다면 조기 종료
    if (target not in words):
        return answer

    N = len(words)
    visited = [0] * N
    q = deque([(begin, 0)])

    while q:
        t, cnt = q.popleft()

        if (t == target):
            answer = cnt
            break

        for idx, w in enumerate(words):
            # 만약 한 글자만 다르다면 큐에 추가하고 탐색
            if (not visited[idx] and checkDecision(t, w)):
                visited[idx] = 1
                q.append([w, cnt + 1])

    return answer

def checkDecision(source, target):
    N = len(source)
    cnt = 0
    for i in range(N):
        if (source[i] != target[i]):
            cnt += 1
        if cnt > 1:
            return False
    return True

print(solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", 	["hot", "dot", "dog", "lot", "log"]))