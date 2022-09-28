'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하라
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로
'''
import sys
input = sys.stdin.readline

N = int(input())    # 주어질 단어의 수
arr = []
for _ in range(N):
    word = input().strip()
    if word not in arr:
        arr.append(word)

[print(word) for word in sorted(arr, key=lambda x: (len(x), x))]
