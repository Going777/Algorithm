N, jinbub = input().split()

alpha_dict = dict()
num = 10
for aschii_num in range(ord('A'), ord('Z')+1):
    alpha_dict.setdefault(chr(aschii_num), num)
    num += 1

result = 0
for idx, digit in enumerate(N[::-1]):
    if digit.isalpha():
        target = int(alpha_dict[digit])
    else:
        target = int(digit) 
    
    result += target * (int(jinbub) ** idx)

print(result) 
