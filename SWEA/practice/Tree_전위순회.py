T = int(input())

def preorder(n):
    if n:
        result.append(n)
        preorder(ch1[n])
        preorder(ch2[n])
    return result

for tc in range(1, T+1):
    V = int(input())    # 트리의 정점 총 개수
    lst = list(map(int, input().split()))
    ch1 = [0] * (V+1)   # 왼쪽 노드 저장
    ch2 = [0] * (V+1)   # 오른쪽 노드 저장
    result = []
    for i in range(0, (V-1)*2, 2):
        p, c = lst[i], lst[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    result = preorder(1)
    print(f"#{tc}", end=" ")
    print(*result)

'''
1
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''