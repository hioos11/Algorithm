# Algorithm

### 템플릿 만들어 놓기

##### 그래프 리스트
```python
list = [[0] * N for _ in range(N)]  # N * N 크기의 0으로 초기화 된 그래프 리스트 생성


list = [[0] * N] # 방식은모든 행이같은 객체로 인식되어 list[1][1]의 값을 변경해도 모든 1열의 값이 같은 값으로 변경됨
```

##### 리스트에서 인덱스 찾기
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
| Original list : [1, 3, 4, 3, 6, 7]
| New indices list : [1, 3]
  - filter를 사용하는 방법도 있지만, enumerate가 더 직관적임


### 백준 티어 골드 이상으로 만들기
