'''
모음(a,e,i,o,u) 하나는 반드시 포함하여야 한다
모음이 3개 혹은 자음이 3개 연속으로 오면 안된다
같은 글자가 연속적으로 오면 안되나, ee와 oo는 허용한다
'''
vowels = ['a','e','i','o','u']
while True:
    password = input()
    if password == 'end':
        break

    prev = ''
    cnt_v = 0
    cnt_c = 0
    check_v = False

    for i in range(len(password)):
        # 이전 글자와 현재 글자가 같은 경우
        if prev == password[i]:
            # 'o', 'e'가 아닌 경우 > not acceptable
            if prev not in ['o', 'e']:
                print(f'<{password}> is not acceptable.')
                break
        # 모음인 경우
        if password[i] in vowels:
            check_v = True
            cnt_v += 1
            cnt_c = 0
        # 자음인 경우
        else:
            cnt_v = 0
            cnt_c += 1

        # 모음 또는 자음이 연속해서 3번 나온 경우 > not acceptable
        if cnt_v == 3 or cnt_c == 3:
            print(f'<{password}> is not acceptable.')
            break
        prev = password[i]
    else:
        # 모음이 한 번이라도 나왔다면 > acceptable
        if check_v:
            print(f'<{password}> is acceptable.')
        # 모음이 안나왔다면 > not acceptable
        else:
            print(f'<{password}> is not acceptable.')

'''
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end
'''