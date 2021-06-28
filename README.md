# Algorithm

### 템플릿 만들어 놓기

#### 그래프 리스트
```python
list = [[0] * N for _ in range(N)]  # N * N 크기의 0으로 초기화 된 그래프 리스트 생성


list = [[0] * N] # 방식은모든 행이같은 객체로 인식되어 list[1][1]의 값을 변경해도 모든 1열의 값이 같은 값으로 변경됨
```

#### 리스트에서 인덱스 찾기
- 인덱스가 하나 일 때 (index)
```python
list.index(element) # list에서 element를 찾아 index값을 반환해줌
```
    - element가 문자나 문자열인 경우 대소문자를 구분
    - 값이 존재하지 않는다면 ValueError 반환



- 인덱스가 여러개 일 때 (enumerate)
```python
test_list = [1, 3, 4, 3, 6, 7]
print("Original list : " + str(test_list))
res_list = [i for i, value in enumerate(test_list) if value == 3]
print("New indices list : " + str(res_list))
```
  > Original list : [1, 3, 4, 3, 6, 7] <br/> New indices list : [1, 3]
  - filter를 사용하는 방법도 있지만, enumerate가 더 직관적임


### 백준 티어 골드 이상으로 만들기



### 런타임에러 발생시 고려 사항
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때
