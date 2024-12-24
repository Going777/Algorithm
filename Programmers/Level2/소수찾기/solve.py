from itertools import permutations
import math

def solution(numbers):
    answer = 0
    num_lst = list(numbers)
    N = len(num_lst)
    
    targets = set()
    for i in range(1, N + 1):
        for p in permutations(num_lst, i):
            target = int("".join(p))
            if target > 0:
                targets.add(target)
        
    for t in targets:
        if is_prime(t):
            answer += 1            
    
    return answer

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:  # 2는 소수
        return True
    if num % 2 == 0:  # 짝수는 소수가 아님
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):  # 3부터 sqrt(num)까지 홀수만 체크
        if num % i == 0:
            return False
    return True