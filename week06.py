class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class Queue:
    def __init__(self):
        self.front = None # 머리
        self.rear = None # 꼬리
        self.size = 0

    def enqueue(self, item):
        self.size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node
        return node.data

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        else:
            self.size -= 1
            temp = self.front
            self.front = self.front.link
            if self.front is None:
                self.rear = None
            temp.link = None
            return temp.data

q = Queue()
print(q.enqueue("data structure"))
print(q.enqueue("data base"))
print(q.enqueue(0))
print(q.enqueue(1))
print(f"size : {q.size}")
print()

for i in range(q.size):
    print(q.dequeue())