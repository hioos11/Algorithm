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