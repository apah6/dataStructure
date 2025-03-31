import random
from os import remove


class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link


class LinkedList:
    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            #print(f"{node.data} ->",end="")
            out_texts = out_texts + str(node.data) + " -> "
            node = node.link
        out_texts += "end"
        return out_texts


    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: #링크드리스트가 노드가 하나도 없는 상태이면 새노드를 헤드에 연결
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link # 다음 노드로 이동
        current.link = Node(data)


    def search(self, target):
        current = self.head
        while current.link:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}은(는) 링크드리스트안에 없습니다."


    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
            previous = current
            current = current.next


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(-9))
print(ll.search(100))
ll.remove(8)
print(ll)