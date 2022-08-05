str = input().upper()
cnt_dict = {}
for c in str:
    if c in cnt_dict.keys():
        continue
    cnt_dict.setdefault(c, str.count(c))

max_cnt = max(cnt_dict.values()) # 딕셔너리 value들 중에서 가장 큰 값 할당
if list(cnt_dict.values()).count(max_cnt) > 1: # max값을 카운팅한 개수가 2이상이면 "?" 출력
    print("?")
else:
    [print(key) for (key, item) in cnt_dict.items() if item == max_cnt] # 이외에는, max값에 해당하는 key값 출력
