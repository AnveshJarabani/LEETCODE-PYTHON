from collections import deque

people= ['Mario', 'Luigi', 'Toad']
queue= deque(people)

queue.append('Browser')
print(queue[1])

queue.popleft()
print(queue)
queue.appendleft('Daisy')
print(queue)
queue.rotate(-1)
print(queue)
queue.extend(['Shyg','Yoshi'])
print(queue)
queue.reverse()
print(queue)