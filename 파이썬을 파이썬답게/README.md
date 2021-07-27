# 파이썬을 파이썬답게
> 프로그래머스 강의 내용 정리<br>파이썬 코드를 low level언어처럼 짜지 않기


## Glossary
- iterable : 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체.
  - list, str, tuple, dict 등
- sequence : int 타입 인덱스를 통해 원소에 접근할 수 있는 iterable. 
  - iterable의 부분집합 느낌.
  - list, str, tuple은 sequence이지만, dict는 다양한 타입을 통해 원소에 접근할 수 있기 때문에 sequence가 아님.


### 1. 몫과 나머지
몫과 나머지를 구할 때 //, %를 사용하는 방법과 divmod를 사용하는 방법이 있다.
- divmod(x, y) : x를 y로 나눈 몫과 나머지를 tuple 형식으로 반환한다.
	- x, y는 복소수가 아닌 숫자.
	- tuple형태를 분리하기 위해 unpacking(*) 사용.

**큰 숫자를 다룰 때에는 divmod가 더 빠르지만, 작은 숫자를 다룰 때에는 //, % 연산자가 더 빠르다**
```python
a = 7
b = 5
print(*divmod(a, b))
print(divmod(a, b))
```
> 1 2 <br>(1, 2)

### 2. n진법 -> 10진법
int(x, base = n) 함수를 사용해 n진수 x를 10진수로 변환 가능
```python
print(int('12', base = 3))
print(int('444', base = 5))
print(int('1010', base = 2))
```
> 5<br/>124<br/>10

### 3. 문자열 정렬하기
길이가 n인 공간에 str을 정렬
- str.ljust(n) : 길이 n에 str을 왼쪽 정렬
- str.center(n) : 길이 n에 str을 가운데 정렬
- str.rjust(n) : 길이 n에 str을 오른쪽 정렬

### 4. string 모듈
몇 가지 데이터들을 상수로 정의해 문자열로 반환
- string.ascii_lowercase : a ~ z까지 알파벳 소문자
- string.ascii_uppercase : A ~ Z까지 알파벳 대문자
- string.ascii_letters : a ~ Z까지 알파벳 소문자, 대문자
- string.digits : 숫자 0 ~ 9
- string.hexdigits : 16진수 0 ~ F
- string.octdigits : 8진수 0 ~ 7

### 5. sorted
sort() 함수를 사용하면 원본 리스트의 원소를 정렬
원본 리스트의 순서를 변경하지 않고 정렬된 데이터를 구하려면 sorted 사용
```python
list1 = [3, 2, 1]
list2 = sorted(list1)
print(list1)
print(list2)
```
> [3, 2, 1]<br/>[1, 2, 3]

### 6. 2차원 리스트 뒤집기 - zip

#### packing 과 unpacking
- packing : 함수가 받을 인자의 갯수를 유연하게 지정. 인자로 받은 여러 개의 값을 하나의 객체(tuple)로 합쳐서 받음
	- 키워드 인자에 패킹을 할 경우 매개변수에 **를 붙인다.
```python
def print_family_name(father, mother, *sibling):
      print("아버지 :", father)
      print("어머니 :", mother)
      if sibling:
           print("호적 메이트..")
           for name in sibling:
                 print(name)
print_family_name("홍길동", '심사임당', '김태희', '윤아')
```
> 아버지 : 홍길동<br/>어머니 : 심사임당<br/>호적 메이트..<br/>김태희<br/>윤아
```python
def kwpacking(**kwargs):
     print(kwargs)
     print(type(kwargs))
kwpacking(a=1, b=2, c=3)
```
> {'a': 1, 'b': 2, 'c': 3}<br/><class 'dict'>
- unpacking : 여러개의 객체를 하나의 객체로 합치는 packing과 반대로 unpacking은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어준다.
```python
def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(sum(*numbers))
```
> 6
- packing을 할 때에는 매개변수에 *을, unpacking 할 때에는 인자 앞에 *를 붙인다.


zip 함수와 unpacking을 사용해 2차원 리스트를 뒤집기
```python
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(new_list)
```
>[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

```python
print(*mylist) # [1, 2, 3] [4, 5, 6] [7, 8, 9]

for a, b, c in zip(*mylist):  # for a, b, c in [1, 2, 3], [4, 5, 6], [7, 8, 9]:
	print(a, b, c)

# 1 4 7
# 2 5 8
# 3 6 9
```
> 2차원 리스트 mylist를 unpacking한 것을 zip으로 묶어 리스트 형태로 만들고(map), 만들어진 세 개의 리스트를 하나의 리스트로 합쳐 2차원 리스트 new_list가 된다.


### 7. i번째 원소와 i+1번째 원소 - zip
```python
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

mylist = [83, 48, 13, 4, 71, 11]
print(solution(mylist))
```
> [35, 35, 9, 67, 60]
- mylist : [83, 48, 13, 4, 71, 11] 
- mylist[1:] : [48, 13, 4, 71, 11]
- zip 함수에 서로 다른 길이의 리스트가 인자로 들어오면 더 짧은 쪽을 기준으로 실행된다.

### 8. 모든 멤버의 type 변환하기 - map
- map은 리스트의 요소를 지정된 함수로 처리해 주는 함수
- map(function, iterable) : interable한 객체의 모든 요소들을 function으로 변경해 객체를 리턴한다.
- 보통 list(map(function, iterable)) 또는 tuple(map(function, iterable))로 반환된 객체를 iterable한 객체로 다시 만들어준다.
```python 
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```
> [1, 100, 33]
```python
def solution(mylist):
    answer = list(map(len, mylist))
    return answer

mylist = [[1, 2], [3, 4], [5]]	
print(solution(mylist))
```
> [2, 2, 1]

### 9. sequence 멤버를 하나로 이어붙이기 - join
- '구분자'.join(리스트) : 매개변수인 리스트의 요소 하나하나 사이에 구분자를 넣어서 문자열로 합쳐준다.
- ''.join(리스트) 방식으로 사용하면 구분자가 없는 형태이므로 리스트 요소 사이에 아무것도 넣지 않고 그냥 리스트의 요소들을 하나의 문자열로 합쳐준다.
```python
my_list = ['1', '100', '33']
answer = ''.join(my_list) # 110033
answer = '_'.join(my_list) # 1_100_33
answer = '\n'.join(my_list)
print(answer)
```
> 1<br/>100<br/>33<br/>

### 10. 삼각형 별찍기 - sequence type의 * 연산
- 곱셈 연산 *를 사용해 문자열 반복 가능
```python
n = 2
answer= [123, 456] * n
print(answer)
```
> [123, 456, 123, 456]

### 11. 곱집합(Cartesian product) 구하기 - product
itertools.product를 사용해 데카르트의 곱을 구할 수 있다.

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
print(list(itertools.product(iterable1, iterable2)))

_list = [1, 2, 3]
print(list(itertools.product(_list, iterable2)))

print(list(itertools.product('ABCD', repeat = 2)))

_list2 = ["012", "abc", "!@#"]
print(list(itertools.product(*_list2)))
```
>[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]<br/>[(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')]<br/>[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]<br/>[('0', 'a', '!'), ('0', 'a', '@'), ('0', 'a', '#'), ('0', 'b', '!'), ('0', 'b', '@'), ('0', 'b', '#'), ('0', 'c', '!'), ('0', 'c', '@'), ('0', 'c', '#'), ('1', 'a', '!'), ('1', 'a', '@'), ('1', 'a', '#'), ('1', 'b', '!'), ('1', 'b', '@'), ('1', 'b', '#'), ('1', 'c', '!'), ('1', 'c', '@'), ('1', 'c', '#'), ('2', 'a', '!'), ('2', 'a', '@'), ('2', 'a', '#'), ('2', 'b', '!'), ('2', 'b', '@'), ('2', 'b', '#'), ('2', 'c', '!'), ('2', 'c', '@'), ('2', 'c', '#')]

### 12. 2차원 리스트를 1차원 리스트로 만들기 - from_iterable
1. sum 함수 사용하기
```python
my_list = [[1, 2], [3, 4], [5, 6]]

answer = sum(my_list, [])
print(answer)
```
> [1, 2, 3, 4, 5, 6]
- sum(iterable, /, start = 0) : iterable 요소들을 왼쪽에서 오른쪽으로 합한 값을 반환하는데, start값도 같이 더해서 반환한다.
	- iterable의 합 + start 값
- 따라서 sum(my_list, []) 에서는 start가 []이기 때문에 start([]) + [1, 2] + [3, 4] + [5, 6]을 연산하여 [1, 2, 3, 4, 5, 6]이 된다.

2. itertools.chain
```python
import itertools

my_list = [[1, 2], [3, 4], [5, 6]]
answer = list(itertools.chain.from_iterable(my_list))
print(answer)
```
> [1, 2, 3, 4, 5, 6]

- itertools.chain() : iterable 객체의 모든 요소들을 
- itertools.chain.from_iterable()


3. itertools, unpacking
```python
my_list = [[1, 2], [3, 4], [5, 6]]
import itertools
answer = list(itertools.chain(*my_list))
print(answer)
```
> [1, 2, 3, 4, 5, 6]

4. list comprehension
```python
my_list = [[1, 2], [3, 4], [5, 6]]
answer = [element for array in my_list for element in array]
print(answer)
```
> [1, 2, 3, 4, 5, 6]


5. reduce - 1
```python 
my_list = [[1, 2], [3, 4], [5, 6]]
from functools import reduce
answer = list(reduce(lambda x, y: x+y, my_list))
print(answer)

```
> [1, 2, 3, 4, 5, 6]


6. reduce - 2
```python
my_list = [[1, 2], [3, 4], [5, 6]]
from functools import reduce
import operator
answer = list(reduce(operator.add, my_list))
print(answer)

```
> [1, 2, 3, 4, 5, 6]


7. numpy 라이브러리 flatten
```python
my_list = [[1, 2], [3, 4], [5, 6]]
import numpy as np
answer = np.array(my_list).flatten().tolist()
print(answer)
```
> [1, 2, 3, 4, 5, 6]




