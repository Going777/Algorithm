text = input()
result = ''
for s in text:
    if not s.isalpha():
        result += s
        continue
    target = ord(s) + 13
		# 소문자, 대문자이면서 범위를 넘어가는 경우 처리 
    if (s.islower() and target > ord('z')) or (s.isupper() and target > ord('Z')):
        target -= 26
    result += chr(target)
print(result)
