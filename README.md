# Algorithm
> 템플릿 만들어 놓기<br>
> 백준 티어 골드 이상으로 만들기<br>
> 
## Python 문법 정리

### list 관련 메소드
- list.index(value) : 리스트에서 value를 찾아 index값 반환
    - 대소문자 구분
    - 값이 존재하지 않으면 ValueError 반환
    - [찾으려는 인덱스가 여러개인 경우](#리스트에서-인덱스-찾기)
- list.extend(list2) : 리스트 뒤에 값을 추가
- list.insert(index, value) : list[index] 뒤에 value 추가
- list.sort() : 오름차순 정렬
- list.reverse() : 내림차순 정렬

#### 리스트와 문자열
- 리스트와 문자열은 유사해서 서로 변환이 가능
  - list = str.split() : 문자열을 리스트로 변환.
  - "".join(list) : 리스트를 문자열로 변환.
    - join 메소드는 매개변수 리스트의 요소 하나하나 사이에 구분자를 끼워 넣어 문자열로 반환한다.

```python
str = "hello world"
list = str.split()
```
> ['hello', 'world']

```python
list = ['1', '2', '3', 'a', 'b', 'c']
str = "구분자".join(list)
```
> 123abc



#### 그래프 리스트
```python
list = [[0] * N for _ in range(N)]  # N * N 크기의 0으로 초기화 된 그래프 리스트 생성


list = [[0] * N] # 방식은모든 행이같은 객체로 인식되어 list[1][1]의 값을 변경해도 모든 1열의 값이 같은 값으로 변경됨
```

#### 리스트에서 인덱스 찾기

- 인덱스가 여러개 일 때 (enumerate)
```python
test_list = [1, 3, 4, 3, 6, 7]
print("Original list : " + str(test_list))
res_list = [i for i, value in enumerate(test_list) if value == 3]
print("New indices list : " + str(res_list))
```
  > Original list : [1, 3, 4, 3, 6, 7] <br/> New indices list : [1, 3]
  - filter를 사용하는 방법도 있지만, enumerate가 더 직관적임


<br><br><br>


## 런타임에러 발생시 고려 사항
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때

<br><br><br>
## 파이썬 코딩테스트 팁
### 재귀함수로 풀 때
```python
import sys
sys.setrecursionlimit(10 ** 6)
```
    이 두 코드를 추가하는 것이 필수적이다.
    파이썬의 기본 재귀 깊이 얕기 때문에 런타임 에러가 발생할 수 있다.
