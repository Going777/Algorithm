# 아이템 줍기

- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/87694)
- Level 3

### 문제

다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.

![](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/9b96b07f-72db-4b1c-bd7a-6a9c9b8d0dc6/rect_1.png)

다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.

![](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/38b0739b-8dd8-40d8-ac44-c71678d28d07/rect_2.png)

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.

![](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ec976181-987e-494e-bb2d-0615ce16252f/rect_4.png)

즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.

다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.

![](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/7eda8d92-ebe0-4b5f-bd15-0c9dc7af3a3e/rect_3.png)

한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

![](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/1e178b0d-6580-4981-aae3-dd82a1b95362/rect_7.png)

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
- rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
  - 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
  - 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
  - 문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
- charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
  - 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
- itemX, itemY는 1 이상 50 이하인 자연수입니다.
  - 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
- 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.

### 입출력 예

| rectangle                                   | characterX | characterY | itemX | itemY | result |
| ------------------------------------------- | ---------- | ---------- | ----- | ----- | ------ |
| `[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]` | 1          | 3          | 7     | 8     | 9      |
| `[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]` | 9          | 7          | 6     | 1     | 11     |
| `[[1,1,5,7]]`                               | 1          | 1          | 4     | 71    | 9      |
| `[[2,1,7,5],[6,4,10,10]]`                   | 3          | 1          | 7     | 10    | 15     |
| `[[2,2,5,5],[1,3,6,4],[3,1,4,6]]`           | 1          | 4          | 6     | 3     | 10     |
