T = 10
for test_case in range(1, T+1):
	dump_cnt = int(input())
	boxes = list(map(int, input().split()))
	result = 0

	cnt = 0
	while cnt <= dump_cnt:
		max_h_i, min_h_i = 0, 0
		for idx in range(len(boxes)): # 리스트 내 최댓값, 최솟값 인덱스 찾기
			if boxes[max_h_i] < boxes[idx]:
				max_h_i = idx
			elif boxes[min_h_i] > boxes[idx]:
				min_h_i = idx

		cnt += 1
		result = boxes[max_h_i] - boxes[min_h_i]

		if result <= 1: # 빠른 종료조건(dump 카운트 내에 평탄화 완료된 경우)
			break

		# 최대 높이 박스를 최소위치로 이동
		boxes[min_h_i] += 1
		boxes[max_h_i] -= 1

	print(f"#{test_case} {result}")
