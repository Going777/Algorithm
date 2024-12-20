import sys
input = sys.stdin.readline

while True:
    nums = sorted(list(map(int, input().split())))
    a, b, c = nums
    result = "Scalene"

    if (a == 0):
        break
        
    if c >= a + b:
        result = "Invalid"
        
    elif a == b == c:
        result = "Equilateral"
    
    elif a == b or b == c:
        result = "Isosceles"
    
    print(result)
