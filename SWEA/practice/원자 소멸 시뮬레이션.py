'''
1. 원자의 최초위치는 [x,y]
2. 원자는 각자 교유의 움직이는 방향을 갖고 있다(상하좌우)
3. 모든 원자들의 이동속도는 동일하다(1초에 1만큼의 거리 이동)
4. 모든 원자들은 최초 위치에서 동시에 이동을 시작한다
5. 두 개 이상의 원자가 동시에 충돌할 경우, 충돌한 원자들은 모두 보유한 에너지 방출 후 소멸한다
0(상), 1(하), 2(좌), 3(우)
원자들이 소멸되면서 방출하는 에너지의 총합은?
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 원자 개수
    atoms = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())   # x위치, y위치, 방향, 보유 에너지
        # x += 1000 ; y += 1000
        atoms.append([x, y, d, k])
    atoms.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(atoms)

    t_energy = 0

    # for _ in range(4000):
    #
    #     # 각 방향으로 원자 위치 옮기기
    #     i = 0
    #     while i < len(atoms):
    #         d = atoms[i][2]
    #         if d == 0:          # 상
    #             atoms[i][1] += 0.5
    #         elif d == 1:        # 하
    #             atoms[i][1] -= 0.5
    #         elif d == 2:        # 좌
    #             atoms[i][0] -= 0.5
    #         else:               # 우
    #             atoms[i][0] += 0.5
    #         if (atoms[i][0]<-2000 or atoms[i][0]>4000) or (atoms[i][1]<-2000 or atoms[i][1]>4000):
    #             atoms.pop(i)
    #         i += 1
    #
    #     # x좌표, y좌표 기준으로 내림차순 정렬
    #     atoms.sort(key=lambda x:(x[0], x[1]), reverse=True)
    #
    #     # 가능한 원자 소멸하기
    #     i = 0 ; j = 1
    #     while atoms and i < len(atoms)-1:
    #         check = False
    #         if (atoms[i][0], atoms[i][1]) == (atoms[j][0], atoms[j][1]):
    #             t_energy += atoms[j][3]
    #             atoms.pop(j)
    #             check = True
    #         else:
    #             j += 1
    #         if check:
    #             t_energy += atoms[i][3]
    #             atoms.pop(i)
    #         if j == len(atoms):
    #             i += 1
    #             j = i + 1
    #
    #     rm_idxs = set()
    #     i = 0 ; j = 1
    #     while atoms and i < len(atoms)-1:
    #         check = False
    #         # x좌표가 같고 & y좌표가 큰 원소는 아래 방향(1), 작은 원소는 위 방향(0)인 경우
    #         if atoms[i][0] == atoms[j][0] and (atoms[i][2] == 1 and atoms[j][2] == 0):
    #             # t_energy += (atoms[i][3] + atoms[j][3])
    #             # atoms.pop(j)
    #             # check = True
    #             # atoms.pop(i)
    #             rm_idxs.add(j)
    #             j = i + 1
    #         # y좌표가 같고 & x좌표가 큰 원소는 왼쪽 방향(2), 작은 원소는 오른쪽 방향(3)인 경우
    #         elif atoms[i][1] == atoms[j][1] and (atoms[i][2] == 2 and atoms[j][2] == 3):
    #             # t_energy += (atoms[i][3] + atoms[j][3])
    #             # atoms.pop(j)
    #             # check = True
    #             # atoms.pop(i)
    #             rm_idxs.add(j)
    #             j = i + 1
    #         # x좌표, y좌표가 모두 같은 경우
    #         elif atoms[i][0] == atoms[j][0] and atoms[i][1] == atoms[j][1]:
    #             # t_energy += (atoms[i][3] + atoms[j][3])
    #             # atoms.pop(j)
    #             # check = True
    #             # atoms.pop(i)
    #             rm_idxs.add(j)
    #             j = i + 1
    #         # 어느 조건에도 해당되지 않는 경우
    #         else:
    #             j += 1
    #         if check:
    #             atoms.pop(i)
    #         if j == len(atoms):
    #             i += 1
    #             j = i+1
    print(f'#{tc} {t_energy}')

'''
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9

1
6
3 5 3 1
7 5 2 1
5 3 0 1
5 7 1 1
6 -4 1 1
9 -7 2 1 
'''