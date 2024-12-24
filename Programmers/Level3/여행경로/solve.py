def solution(tickets):
    answer = []
    tickets.sort()
    N = len(tickets)
    visited= [False] * N

    def dfs(airport, path):
        if (len(path) == N + 1):
            answer.append(path)
            return
        
        for idx, (f, t) in enumerate(tickets):
            if (f == airport and not visited[idx]):
                visited[idx] = True
                dfs(t, path + [t])
                visited[idx] = False
    
    dfs("ICN", ["ICN"])

    return answer[0]

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])