# Algorithm
> 템플릿 만들어 놓기<br>
> 백준 티어 골드 이상으로 만들기<br>
> 
## 1. Python 문법 정리

### 1. list 관련 메소드
- list.index(value) : 리스트에서 value를 찾아 index값 반환
    - 대소문자 구분
    - 값이 존재하지 않으면 ValueError 반환
    - [찾으려는 인덱스가 여러개인 경우](#리스트에서-찾으려는-value가-여러-개인-경우-인덱스-찾기)
- list.extend(list2) : 리스트 뒤에 값을 추가
- list.insert(index, value) : list[index] 뒤에 value 추가
- list.sort() : 오름차순 정렬 (#9.-sort와-sorted)
- list.reverse() : 내림차순 정렬
- list[-1] : list.pop()을 하면 가장 마지막 원소를 제거하고 가져오지만 제거하지 않고 가져만 올 때에는 [-1]을 사용한다.

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

<br><br>

#### 그래프 리스트
```python
# N * N 크기의 0으로 초기화 된 그래프 리스트 생성
list = [[0] * N for _ in range(N)]  

# 이 방식은 모든 행이 같은 객체로 인식되어 
# list[1][1]의 값을 변경해도 모든 1열의 값이 같은 값으로 변경됨
list = [[0] * N] 
```

#### 리스트에서 찾으려는 value가 여러 개인 경우 인덱스 찾기

- enumerate 사용
- filter를 사용하는 방법도 있지만, enumerate가 더 직관적임
```python
# test_list에서 value가 3인 인덱스를 모두 찾아 res_list에 인덱스 저장
test_list = [1, 3, 4, 3, 6, 7]
print("Original list : " + str(test_list))
res_list = [i for i, value in enumerate(test_list) if value == 3]
print("New indices list : " + str(res_list))
```
  > Original list : [1, 3, 4, 3, 6, 7] <br/> 
  > New indices list : [1, 3]


### 2. 문자열 관련 메소드
- str.replace("검색 문자", "치환 문자" [, 치환 횟수]) : str에 "검색 문자"가 있다면 "치환 문자"로 바꿔준다
	- 검색 문자 : 문자열에서 찾을 문자를 지정
	- 치환 문자 : 변경하고 싶은 문자
	- 치환 횟수 : 치환하고 싶은 횟수(생략 가능)
```python
text = "orange, apple, melon, orange, grape, orange"
text_replace = text.replace("orange", "banana", 2)
```
> banana, apple, melon, banana, grape, orange<br>text에는 "orange"가 3개 있지만 치환 횟수를 2로 지정했기 떄문에 앞에서 두 개만 "banana"로 치환된다.
- index = str.find(문자, 시작위치) : 문자열 str의 인덱스 2부터 문자를 찾아 인덱스를 반환한다. 만약 시작위치가 생략되면 인덱스 0인 처음부터 찾는다.
	- 찾지 못하는 경우, -1을 반환 (_리스트 메소드인 index와 다른 점_)
	- rfind를 사용하면 뒤에서부터 찾을 수 있다.

### 3. zip
- 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소에 차례로 접근할 수 있는 반복자(iterator)를 반환한다.
- 만약, zip으로 넘기는 인자의 길이가 서로 다른 경우 짧은 인자를 기준으로 데이터가 묶이고 나머지는 버려진다.
```python
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']

for pair in zip(numbers, letters):
	print(pair)
```
> (1, 'a')<br>(2, 'b')<br>(3, 'c')

#### unzip
- zip() 함수로 묶어 놓은 데이터를 다시 해체할 때 사용
```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
pairs = list(zip(numbers, letters))
```
>[(1, 'a'), (2, 'b'), (3, 'c')]
- 리스트 앞에 unpacking 연산자(*)를 붙여 zip()함수에 넘기면 분리되어 반환된다.
```python
numbers, letters = zip(*pairs)
```
>(1, 2, 3) ('a', 'b', 'c')

#### zip -> dict
- 두 개의 리스트를 zip() 함수를 통해 하나로 묶어 dictionary로 쉽게 만들 수 있다.


### 4. collections


### 5. enumerate
- 반복문을 사용할 때 몇번째 반복문인지 확인 가능
- (인덱스번호, 원소) tuple형태로 반환
```python
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
    print(p)
```
> (0, 1)<br>(1, 5)<br>(2, 7)<br>(3, 33)<br>(4, 39)<br>(5, 52)

### 6. 아스키코드
- 문자 -> 아스키코드 : ord(65)	=> A
- 아스키코드 -> 문자 : chr('A')	=> 65

### 7. 순열과 조합
#### 순열
	- n개의 원소를 사용해 순서를 정하여 r개의 배열로 나타내는 것.
	- 순서가 있어 원소의 종류가 같아도 순서가 다르면 다른 배열.
	- nPr = n! / (n-r)!
```python
from itertools import permutations

a = [1, 2, 3]
p = permutations(a, 2)
print(list(p))	
```
> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#### 조합
	- n개의 원소를 사용해서 순서에 관계없이 r개의 배열로 나타내는 것.
	- 순서가 없어 원소의 종류가 같으면 같은 배열.
	- nCr = nPr / r!
```python
from itertools import combinations

a = [1, 2, 3]
c = combinations(a, 2)

print(list(c))
```
> [(1, 2), (1, 3), (2, 3)]


### 8. 딕셔너리


### 9. sort와 sorted
- sort는 **list.sort()** 방식으로 사용해 리스트 자체가 정렬된다.
- sorted는 sorted_list = sorted(list) 방식으로 사용되며 list 자체는 정렬되지 않고 list가 정렬된 결과가 반환되어 sorted_list에 저장된다.

### 10. swap
- 다른 언어와 다르게 python은 두 변수의 값을 바꿀 때 별도의 변수가 필요 없다.
- a, b = b, a 한 줄로 a와 b를 바꿀 수 있다.

<br><br><br>
## 2. 알고리즘 분류

1. 우선순위 큐(Priority Queue)
- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 데이터를 우선순위에 따라 처리하고 싶을 때 사용
- 완전 이진 트리의 일종으로 항상 루트 노드를 제거
- 최소 힙 : 루트 노드가 가장 작은 값을 가져 값이 작은 데이터가 우선적으로 제거
- 최대 힙 : 루트 노드가 가장 큰 값을 가져 값이 큰 데이터가 우선적으로 제거

2. 

## 3. 런타임에러 발생시 고려 사항
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때

<br><br><br>
## 4. 파이썬 코딩테스트 팁
### 재귀함수로 풀 때
```python
# 파이썬의 기본 재귀 깊이가 얕기 때문에 런타임 에러가 발생할 수 있다.
# 따라서 이 두 코드를 추가하는 것이 필수적이다.
import sys
sys.setrecursionlimit(10 ** 6)
```
    
