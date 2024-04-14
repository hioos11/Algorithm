'''
queue는 arraylist로 구현할 수도, linked list로 구현할 수 도 있다.
array list로 구현하는 방법에는 단순히 array를 이용하는 방법과 circular queue를 만드는 방법, dynamic array를 만든느 방법이 있다.
하지만 arraylist로 queue를 구현하는데에는 장점이 딱히 없어서(시간복잡도의 문제가 있다.) linked list를 베이스로 구현하는 queue를 사용한다.
매번 구현하지 않고 파이썬에 구현되어 있는 deque라는 자료구조를 이용한다.

Queue의 정의
queue는 시간 순서상 먼저 저장한 데이터가 먼저 출력되는 선입선출 FIFO(First In First Out)의 형식으로 데이터를 저장하는 자료구조이다.
rear, front가 각각 마지막 데이터, 첫번째 데이터를 가리키고 rear에 데이터를 추가하면 enqueue, front에서 데이터를 꺼내면 dequeue라고 한다.

queue를 array list로 구현을 한다면 enqueue의 경우 단순히 list.append(value)를 사용해 구현해 O(1)의 시간복잡도를 가지지만
dequeue의 경우 list.pop(0)으로 구현 후 idx=0의 value를 뽑아낸거기 때문에 idx=1이후의 value들을 한칸씩 앞으로 이동시켜주는 작업이 필요하다.
따라서 O(n)의 시간복잡도를 가진다.

파이썬에서는 linked list로 구현된 deque 자료구조가 있다.
일반적으로 queue는 front에서만 dequeue가 가능하고 rear에서만 enqueue가 가능한데, 
파이썬의 deque는 front에서도 enqueue, dequeue가 가능하고 rear에서도 enqueue,dequeue가 가능하다.
d(doubly)e(ended)que(queue)의 의미를 가져 앞뒤에서 enqueue, dequeue 모두 가능하다. 
double linked list로 구현되어있기 때문에 enqueue, dequeue모두 O(1)의 시간복잡도를 가진다.

코딩테스트에서 queue는 보통 단독으로 사용되지는 않고 bfs라는 알고리즘을 구현하는데 많이 사용된다.

'''