def solve():
    need_card = []
    for idx in range(0, len(S), 3):
        num = int(S[idx+1:idx+3])

        if num in card_dict[S[idx]]:
            return "ERROR"

        card_dict[S[idx]].append(num)


    for p in card_dict.values():
        need_card.append(13 - len(p))

    return need_card

T = int(input())
for tc in range(1, T+1):
    S = input()
    card_dict = {"S":[],"D":[],"H":[],"C":[]}

    ans = solve()

    if ans == "ERROR":
        print(f"#{tc}", ans)
    else:
        print(f"#{tc}", *ans)

'''
3
S01D02H03H04
H02H10S11H02
S10D10H10C01
'''