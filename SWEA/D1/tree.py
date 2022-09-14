'''
정점 번호 V : 1~(E+1)번까지
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

# 전위순회
def preorder(n):
    if n:
        print(n)   # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)   # visit(n)
        inorder(ch2[n])

# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)   # visit(n)

E = int(input())   # 간선수
arr = list(map(int, input().split()))
V = E+1
root = 1

# 1. 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 2. 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

for i in range(0, E*2, 2):
    p, c = arr[i], arr[i+1]
    if ch1[p] == 0:  # 아직 자식이 없으면
        ch1[p] = c   # 자식1로 저장
    else:            # 자식1에 이미 값이 있다면
        ch2[p] = c   # 자식2로 저장
    par[c] = p

# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)
# print()

root = find_root(V)
print(root)



