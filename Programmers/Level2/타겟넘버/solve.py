from collections import deque

answer = 0
def solution(numbers, target):
    global answer
    # bfs(numbers, target)
    dfs(numbers, target, 0, 0)
    return answer

def bfs(numbers, target):
    global answer
    N = len(numbers)
    q = deque([(0, 0)])
    
    while q:
        i, sm = q.popleft()
        if (i == N):
            if (sm == target):
                answer += 1
            continue

        for k in (numbers[i], -numbers[i]):
            q.append([i+1, sm + k])


def dfs(numbers, target, idx, sm):
    global answer
    if (idx == len(numbers)):
        if (sm == target):
            answer += 1
        return
    
    for k in (numbers[idx], -numbers[idx]):
        dfs(numbers, target, idx + 1, sm + k)

solution([1,1,1,1,1], 3)
print(answer)