# 표 크기는 50X50
# UPDATE
    # UPDATE r c v : (r,c) 좌표에 v 삽입
    # UPDATE v1 v2 : v1을 v2로 치환
# MERGE
    # MERGE r1 c1 r2 c2 : (r1,c1) 값을 (r2,c2)에 똑같이 적용
# UNMERGE
    # UNMERGE r c : (r,c)에 해당한 모든 병합 해제 -> 실행 초기 상태로
# PRINT
    # PRINT r c : (r,c) 값 출력 / 비었다면 "EMPTY"

graph = [[[]*50]*50 for _ in range(50)]
graph_val = [["EMPTY"]*50 for _ in range(50)]

for i in range(50):
    for j in range(50):
        graph[i][j] = (i, j)

def solution(commands):
    ans = []
    for command in commands:
        state = command.split()
        cmd = state[0]

        if cmd == "UPDATE":
            if len(state) == 4:
                r, c, v = int(state[1])-1, int(state[2])-1, state[3]
                graph_val[r][c] = v
            else:
                v1, v2 = state[1], state[2]
                for i in range(50):
                    for j in range(50):
                        if graph_val[i][j] == v1:
                            graph_val[i][j] = v2
        elif cmd == "MERGE":
            r1, c1, r2, c2 = int(state[1])-1, int(state[2])-1, int(state[3])-1, int(state[4])-1
            graph[r2][c2] = [r1,c1]
        elif cmd == "UNMERGE":
            r, c = int(state[1])-1, int(state[2])-1
            for i in range(50):
                for j in range(50):
                    if graph[r][c] == [r,c]:
                        graph[r][c] = []
        else:
            r, c = int(state[1])-1, int(state[2])-1
            if not graph[r][c]:
                ans.append(graph_val[r][c])
            else:
                nr, nc = graph[r][c]
                ans.append(graph_val[nr][nc])
    print(ans)
    print(graph)
    print(graph_val)
    return ans


solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])