from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()


def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue("1")

    for i in range(number):
        result.append(queue.dequeue())
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result  # For number = 3, result = {"1", "10", "11"}


print(find_bin(3))  # Testing with 3 to match your comment
