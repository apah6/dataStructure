class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            return
        current = self.root
        while(True):
            if(current.data > data):
                if(current.left is None):
                    current.left = newNode
                    return
                current = current.left
            elif(current.data < data):
                if (current.right is None):
                    current.right = newNode
                    return
                current = current.right
            else:
                return



asd = BST()

asd.insert(100)
asd.insert(25)
asd.insert(10)
asd.insert(49)
asd.insert(48)
asd.insert(60)

print(asd.root.left.right.left.data)