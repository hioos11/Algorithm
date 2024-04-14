'''
queue와는 다르게 stack자체로도 코딩 테스트 문제에 많이 나온다.
또한 다른 알고리즘을 구현하는 자료구조에도 많이 사용된다.

stack은 array list를 사용해도 O(1)의 시간복잡도를 가져 굳이 linked list를 사용하지 않는다.

Stack의 정의
stack은 시간 순서상 가장 최근에 추가한 데이터가 가장 먼저 나오는 후입선출 LIFO(Last In First Out)형식으로 데이터를 저장하는 자료구조이다.
stack의 top에 데이터를 추가하는 것을 push, top에서 데이터를 추출하는 것을 pop이라 한다.


Stack의 활용
1. LIFO 특성을 활용한 문제
2. DFS(깊이 우선 탐색)에 사용


가장 대표적인 유형 중 '괄호 유효성 문제'가 있다. (Valid Parentheses)
'''