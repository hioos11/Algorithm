# 파이썬에서 기본으로 제공하는 힙 라이브러리는 min-heap으로 동작하여 오름차순 정렬됨 

import sys
import headq
input = sys.stdin.readline

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

n = int(input())
arr = []

for i in range(n):
  arr.append(int(input())
res = heapsort(arr)
             
for i in range(n):
    print(res[i])
