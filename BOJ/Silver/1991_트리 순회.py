import sys
input = sys.stdin.readline

def preorder(n):
    if n:
        print(chr(n), end='')
        preorder(ch1[n-ord("A")])
        preorder(ch2[n-ord("A")])

def inorder(n):
    if n:
        inorder(ch1[n-ord("A")])
        print(chr(n), end='')
        inorder(ch2[n-ord("A")])

def postorder(n):
    if n:
        postorder(ch1[n - ord("A")])
        postorder(ch2[n - ord("A")])
        print(chr(n), end='')

N = int(input())    # 노드 개수
ch1 = [0] * N
ch2 = [0] * N
for i in range(N):
    V, L, R = input().split()
    if L != ".":
        ch1[ord(V)-ord("A")] = ord(L)
    if R != ".":
        ch2[ord(V)-ord("A")] = ord(R)

preorder(ord("A"))
print(end='\n')
inorder(ord("A"))
print(end='\n')
postorder(ord("A"))

'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''